from django.urls import path

from . import views

urlpatterns = [
    path("tasks", views.TasksHomeView.as_view(), name="home"),
]