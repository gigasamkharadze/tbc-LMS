from django.urls import path
from academic_portal.views import ChooseCourseView, CourseStudentsView, SuccessView, home, add_course, AssignmentView
app_name = 'academic_portal'

urlpatterns = [
    path('', home, name='home'),
    path('add_course/', add_course, name='add_course'),
    path('assignment/', AssignmentView.as_view(), name='assignment'),
    path('choose_course/', ChooseCourseView.as_view(), name='choose_course'),
    path('attendance_registration/<str:course_code>/', CourseStudentsView.as_view(), name='attendance_registration'),
    path('success/<str:course_code>/', SuccessView.as_view(), name='success_page'),
]
