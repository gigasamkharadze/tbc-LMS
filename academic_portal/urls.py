
from django.urls import path
from academic_portal.views import home, add_course, AssignmentView

app_name = 'academic_portal'

urlpatterns = [
    path('', home, name='home'),
    path('add_course/', add_course, name='add_course'),
    path('assignment/', AssignmentView.as_view(), name='assignment'),
]
