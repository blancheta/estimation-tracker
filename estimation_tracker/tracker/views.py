from django.shortcuts import redirect, render
from django.views.generic import View
from tracker.forms import TaskForm
from tracker.models import Task


class TasksHomeView(View):
    template_name = "home.html"
    form_class = TaskForm

    def get(self, request, task_id = None):
        context = {"tasks": Task.objects.all(), "form": self.form_class()}
        
        if task_id:
            task = Task.objects.get(id=task_id)
            context["form"] = self.form_class(instance=task)
            
        return render(request, self.template_name, context)

    def post(self, request, task_id = None):
        
        if task_id:
            task = Task.objects.get(id=task_id)
            form = self.form_class(request.POST, instance=task)
        else:
            form = self.form_class(request.POST)

        if form.is_valid():    
            form.save()
            return redirect('home')
        
        context = {"tasks": Task.objects.all(), "form": self.form_class()}
        return render(request, self.template_name, context)
