
from django.urls import path

from . import views

app_name = 'esttracker'

urlpatterns = [
    path('', views.TaskCreateListView.as_view(), name='task_create_list'),
]