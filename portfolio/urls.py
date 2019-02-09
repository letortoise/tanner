from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("project1", views.project1_view, name="project1"),
    path("project2", views.project2_view, name="project2"),
    path("project3", views.project3_view, name="project3")
]
