from django.shortcuts import render
from .models import Task
from .forms import CreateTask
from django.views.generic import  CreateView
from django.urls import reverse_lazy


class TaskCreateListView(CreateView):
    model = Task
    template_name = 'task_create_list.html'
    form_class = CreateTask
    success_url = reverse_lazy('esttracker:task_create_list')

    def get_context_data(self, **kwargs):
        context = super(TaskCreateListView, self).get_context_data(**kwargs)
        context["tasks"] = Task.objects.all().order_by('created_at')
        return context
