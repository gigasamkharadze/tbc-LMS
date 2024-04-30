# accounts/urls.py
from django.urls import path

from .views import SignUpView, logout_view

app_name = "users"

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('logout/', logout_view, name='logout'),
]
