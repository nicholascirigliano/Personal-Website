from django.urls import path
from . import views
#from .views import ProjectView

urlpatterns = [
    path('', views.home, name="home"),
    path('projects/', views.project, name="projects")
]