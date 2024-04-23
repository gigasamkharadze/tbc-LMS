from django.shortcuts import redirect, render
from academic_portal.models import Faculty
from academic_portal.forms import CourseForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def add_course(request):
    user = request.user
    student = user.student
    num_courses = student.courses.count()
    context = {
        'courses': student.courses.all(),
        'first_name': student.first_name,
        'last_name': student.last_name,
        'faculty': student.faculty,
        'all_courses': student.faculty.courses.all()
    }
    if user.is_authenticated:
        if num_courses < 7:
            if request.method == 'POST':
                course = request.POST.get('course')
                course = get_object_or_404(Course, code=course)
                user.student.courses.add(course)
            #     go to the same page
                return redirect('academic_portal:add_course')
            else:
                return render(request, 'add_course.html', context)
        else:
            return render(request, 'add_course1.html', context)
    else:
        form = CourseForm()
        faculties = Faculty.objects.all()  
    return render(request, 'subjectform.html', {'form': form, 'faculties': faculties})