from django.urls import path

from . import views

urlpatterns = [
    path("", views.TaskCreateListView.as_view(), name="task_create_list"),
]
