from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import logout
from users.forms import CustomUserCreationForm
from django.shortcuts import redirect


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def logout_view(request):
    logout(request)
    return redirect("home")
