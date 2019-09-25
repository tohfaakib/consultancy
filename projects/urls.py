from django.urls import path, include
from .views import projects, projects_detail

urlpatterns = [
    path('projects/', projects, name='projects'),
    path('projects/<int:pk>/', projects_detail, name='projects_detail')
]