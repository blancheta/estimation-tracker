from audioop import reverse
from django.shortcuts import redirect, render
from django.views.generic import View
from tracker.forms import TaskForm
from tracker.models import Task


class TasksHomeView(View):
    template_name = "home.html"
    form_class = TaskForm

    def get(self, request):
        context = {"tasks": Task.objects.all(), "form": self.form_class()}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
        
        context = {"tasks": Task.objects.all(), "form": self.form_class()}
        return render(request, self.template_name, context)
