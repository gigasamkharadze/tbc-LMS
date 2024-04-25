from django import forms
from academic_portal.models import Assignment


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'description', 'due_date', 'course']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }
