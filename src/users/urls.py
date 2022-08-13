from django.urls import path

from users.views import login_user, register_user, auth_callback, logout


app_name = "users"

urlpatterns = [
    path("register", register_user, name="register"),
    path("login", login_user, name="login"),
    path("auth-callback", auth_callback, name="auth-callback"),
    path("logout", logout, name="logout")
]
