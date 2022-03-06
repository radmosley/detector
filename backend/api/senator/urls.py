from django.urls import path
from . import views

urlpatterns = [
    path('senator/', views.Senators),
]