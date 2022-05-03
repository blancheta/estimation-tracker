from django.shortcuts import redirect, render
from django.views.generic import View
from tracker.forms import TaskForm
from tracker.models import Task

class HomeView(View):
    template_name = 'home.html'
    
    def get(self, request):
        context = {
            'tasks': Task.objects.all()
        }
        return render(request, self.template_name, context)


class FormView(View):
    form_class = TaskForm
    template_name = 'create_task.html'
    
    def get(self, request, *args, **kwargs):            
        context = {
            'form' : self.form_class
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('home')
        
        context = {'form': form}
        return render(request, self.template_name, context)
