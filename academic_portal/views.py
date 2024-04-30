from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.db import transaction
from academic_portal.models import Course
from academic_portal.forms import AssignmentForm, AttendanceForm
from users.models import CustomUser
from datetime import date


@login_required
def home(request):
    assignments = []
    if hasattr(request.user, 'lecturer'):
        courses = request.user.lecturer.courses.all()
        for course in courses:
            assignments = assignments + list(course.assignments.all())
    return render(request, 'home1.html', {
        'user': request.user,
        'assignments': assignments
    })


def add_course(request):
    user = request.user
    if user.is_authenticated:
        if request.method == 'POST':
            course = request.POST.get('course')
            course = get_object_or_404(Course, code=course)
            if user.student.courses.filter(code=course.code).exists() or user.student.courses.count() >= 7:
                return redirect('academic_portal:add_course')
            user.student.courses.add(course)
            return redirect('academic_portal:add_course')
        else:
            if hasattr(user, 'student'):
                student = user.student
                return render(request, 'add_course.html', {
                    'courses': student.courses.all(),
                    'first_name': student.first_name,
                    'last_name': student.last_name,
                    'faculty': student.faculty,
                    'all_courses': student.faculty.courses.all()
                })
            else:
                return render(request, 'not_student.html')
    else:
        return redirect('login')


class AssignmentView(View):
    @staticmethod
    def get(request):
        user = request.user
        if user.is_authenticated:
            if hasattr(user, 'student'):
                if hasattr(user, 'student'):
                    form = AssignmentForm()
                    return render(request, 'student_assignment_submission.html', {'form': form})
            elif hasattr(user, 'lecturer'):
                return render(request, 'create_assignment.html', {
                    'form': AssignmentForm(lecturer=user.lecturer)
                })
        else:
            return redirect('login')

    @staticmethod
    def post(request):
        user = request.user
        if user.is_authenticated:
            if hasattr(user, 'student'):
                form = AssignmentForm(request.POST, request.FILES)
                if form.is_valid():
                    form.save()
                    return redirect('academic_portal:home')
                return render(request, 'student_assignment_submission.html', {'form': form})
            elif hasattr(user, 'lecturer'):
                form = AssignmentForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('academic_portal:home')
                return render(request, 'create_assignment.html', {
                    'form': form
                })
        else:
            return redirect('login')


class ChooseCourseView(View):
    @staticmethod
    def get(request):
        if request.user.is_authenticated and hasattr(request.user, 'lecturer'):
            lecturer = request.user.lecturer
            courses = lecturer.courses.all()
            return render(request, 'choose_course.html', {'courses': courses})
        else:
            return redirect('login')


class CourseStudentsView(View):
    @staticmethod
    def get(request, course_code):
        course = Course.objects.get(code=course_code)
        students = course.students.all()
        current_date = date.today()
        form = AttendanceForm()
        return render(request, 'attendance_registration.html',
                      {
                          'form': form,
                          'course': course,
                          'students': students,
                          'current_date': current_date
                      })

    @staticmethod
    def post(request, course_code):
        course = Course.objects.get(code=course_code)
        students = course.students.all()
        current_date = request.POST.get('date', date.today())
        data = request.POST.copy()
        data['course'] = course
        form = AttendanceForm(data=data)
        form.is_valid(raise_exception=True)
        if form.is_valid():
            with transaction.atomic():
                attendance = form.save()
                student_emails = request.POST.getlist('students_attended')

                attended_students = CustomUser.objects.filter(email__in=student_emails)
                for student in attended_students:
                    attendance.students_attended.add(student)
                return render(request, 'success_page.html', {'course': course})
        else:
            return render(request, 'attendance_registration.html',
                          {
                              'form': form,
                              'course': course,
                              'current_date': current_date,
                              'students': students
                          })


class SuccessView(View):
    @staticmethod
    def get(request, course_code):
        course = Course.objects.get(pk=course_code)
        return render(request, 'success_page.html', {'course': course})
