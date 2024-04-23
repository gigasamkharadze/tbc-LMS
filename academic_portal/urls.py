
from django.urls import path
from academic_portal.views import home, add_course


urlpatterns = [
    path('', home, name='home'),
    path('add_course/', add_course, name='add_course'),
    path('add_course1/', add_course, name='courses'),
]
