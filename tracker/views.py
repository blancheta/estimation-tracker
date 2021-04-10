from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .models import Task
from .forms import *
from datetime import datetime, timedelta

# Create your views here.
# This method (1)
class TaskView(TemplateView):
    template_name = 'tracker/home.html'

    
    def get(self, request):
        data = Task.objects.all()
        context = {'data':data,}
        return render (request,self.template_name, context)

    def post(self, request):
        name = request.POST['name']
        planning = request.POST['planning']
        estimated = request.POST['estimated']
        real = request.POST['real']
        risk = request.POST['risk']
        level = request.POST['level']
        notes = request.POST['notes']

        estimated_dt = datetime.strptime(estimated, '%H:%M')

        realtime_dt = datetime.strptime(real, '%H:%M')

        estimated_duration_td = timedelta(hours=estimated_dt.hour, minutes=estimated_dt.minute)
        realtime_duration_td = timedelta(hours=realtime_dt.hour, minutes=realtime_dt.minute)

        diff_td = realtime_duration_td - estimated_duration_td
        seconds = diff_td.seconds
        calc = f"{int(seconds / 3600)}"+f': {(int(seconds / 60)) % 60} '
        correctness = 100 * realtime_duration_td.seconds / estimated_duration_td.seconds

        table = Task(name=name,
        planning=planning,
        estimate=estimated,
        realtime=real,
        risk=risk,
        level=level,
        notes=notes,
        estimateb_by_calc=calc,
        correctness=correctness,
        )
        table.save()
        return redirect('/')



# Or this (2)
"""
def home(request):
    form = DataForm()
    if request.method == "POST":
        form = DataForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')

    data = Task.objects.all()
    context = {'data': data, 'form': form}
    return render(request, 'tracker/home.html', context)
"""