from django.shortcuts import redirect, render
from tracker.forms import TaskForm
from tracker.models import Task
    
def home(request):
    
    context = {
        'tasks': Task.objects.all()
    }
    
    return render(request, 'home.html', context)


def create_task(request):
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        
        if form.is_valid():
            form.save()

        return redirect('home')
    
    context = {
        'form' : TaskForm()
    }
    
    return render(request, 'create_task.html', context)