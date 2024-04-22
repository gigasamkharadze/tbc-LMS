from django.shortcuts import redirect, render, get_object_or_404

from academic_portal.models import Course


# Create your views here.
def home(request):
    return render(request, 'home1.html')


def add_course(request):
    user = request.user
    if user.is_authenticated:
        if request.method == 'POST':
            course = request.POST.get('course')
            course = get_object_or_404(Course, code=course)
            user.student.courses.add(course)
        #     go to the same page
            return redirect('academic_portal:add_course')
        else:
            student = user.student
            return render(request, 'add_course.html', {
                'courses': student.courses.all(),
                'first_name': student.first_name,
                'last_name': student.last_name,
                'faculty': student.faculty,
                'all_courses': student.faculty.courses.all()
            })
    else:
        return redirect('login')
