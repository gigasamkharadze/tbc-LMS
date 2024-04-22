

from django import forms
from academic_portal.models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'syllabus']
