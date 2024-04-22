from django.shortcuts import redirect, render
from academic_portal.models import Faculty
from academic_portal.forms import CourseForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CourseForm()
        faculties = Faculty.objects.all()  
    return render(request, 'subjectform.html', {'form': form, 'faculties': faculties})