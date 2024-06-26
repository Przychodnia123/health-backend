from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path("login/", obtain_auth_token, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.user_register_view, name="register"),
    path("dashboard/", views.Dashboard.as_view())
]