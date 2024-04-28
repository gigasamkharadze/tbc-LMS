from datetime import date
from django import forms
from academic_portal.models import Assignment, Attendance, Course
from rest_framework import serializers


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'description', 'due_date', 'course']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['code', 'title', 'description', 'syllabus']


class AttendanceForm(forms.ModelForm):
    
    class Meta:
        model = Attendance
        fields =  ['date', 'course', 'students_attended']

class AttendanceForm(serializers.ModelSerializer):
    class Meta:        
        model =  Attendance        
        fields = ['date', 'course']
