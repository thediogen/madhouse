from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView

from .forms import CustomAuthForm, RegistrationForm



class CustomLoginView(LoginView):
    authentication_form = CustomAuthForm
    template_name = "login.html"


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")

    form = RegistrationForm()

    return render(request, "register.html", context={"register_form": form})


def logout_user(request):
    logout(request)
    return redirect("/")