"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path("", views.home, name="home")
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path("", Home.as_view(), name="home")
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path("blog/", include("blog.urls"))
"""
from django.contrib import admin
from .senator.views import Users, Register, Senators, Login, Logout, AuthenticatedUser
from django.urls import path

# router = DefaultRouter()
# router.register("senator/", views.SenatorViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("senators/", Senators),
    path("users/", Users),
    path("register/", Register),
    path("login/", Login),
    path("logout/", Logout),
    path("user/", AuthenticatedUser.as_view()),
]
