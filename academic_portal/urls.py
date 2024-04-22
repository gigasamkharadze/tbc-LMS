
from django.urls import path
from academic_portal.views import home, add_course


urlpatterns = [
    path('', home, name='home'),
    path('add-course/', add_course, name='add_course')
]
