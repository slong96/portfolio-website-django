from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('resume/', views.resume, name='resume-page'),
    path('projects/', views.projects, name='projects-page'),
]