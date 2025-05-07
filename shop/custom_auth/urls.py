from django.urls import path
from .views import CustomLoginView, register,logout_user

urlpatterns = [
    path("login", CustomLoginView.as_view(), name="login"),
    path("register", register, name="register"),
    path("logout", logout_user, name="logout")
]