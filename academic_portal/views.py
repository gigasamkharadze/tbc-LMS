from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View

from academic_portal.models import Course
from academic_portal.forms import AssignmentForm


# Create your views here.
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
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            if hasattr(user, 'student'):
                if hasattr(user, 'student'):
                    form = AssignmentForm()
                    return render(request, 'student_assignment_submission.html', {'form': form})
            elif hasattr(user, 'lecturer'):
                return render(request, 'create_assignment.html', {
                    'form': AssignmentForm()
                })
        else:
            return redirect('login')

    def post(self, request):
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
