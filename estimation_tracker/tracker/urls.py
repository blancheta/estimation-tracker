from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("create_task", views.FormView.as_view(), name="create_task"),
]