
from django.urls import path
from academic_portal.views import home, add_course

app_name = 'academic_portal'

urlpatterns = [
    path('', home, name='home'),
    path('add_course/', add_course, name='add_course')
]
