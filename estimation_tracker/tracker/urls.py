from django.urls import path

from . import views

urlpatterns = [
    path("tasks", views.TasksHomeView.as_view(), name="home"),
    path("tasks/<int:task_id>", views.TasksHomeView.as_view(), name="edit_form"),
]