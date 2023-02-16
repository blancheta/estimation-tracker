from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import BaseCreateView

from .forms import CreateTask
from .models import Task


class TaskCreateListView(BaseCreateView, ListView):
    model = Task
    template_name = "task_create_list.html"
    form_class = CreateTask
    success_url = reverse_lazy("task_create_list")

    def get_queryset(self):
        return Task.objects.all().order_by("created_at")
