from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Task
from .forms import *
from .utils import *

# Create your views here.
# This method (1)
"""
class TaskView(TemplateView):
    template_name = 'tracker/home.html'

    # get: displays the page and the data therein
    def get(self, request):
        data = Task.objects.all()
        # averaging
        total_correctness = 0
        liste = []
        for _data in data:
            liste.append(_data.correctness)
        for x in liste:
            total_correctness = x + total_correctness

        moyenne_correctness = round(total_correctness / len(liste), 3)

        context = {'data':data, 'moyenne_correctness': moyenne_correctness}
        return render (request,self.template_name, context)

    # post: retrieves the form data to save and reload the home page
    def post(self, request):
        name = request.POST['name']
        planning = request.POST['planning']
        estimated = request.POST['estimated']
        real = request.POST['real']
        risk = request.POST['risk']
        level = request.POST['level']
        notes = request.POST['notes']

        # calculation of estimateb_by_calc and correctness from user data
        estimated_dt = datetime.strptime(estimated, '%H:%M')

        realtime_dt = datetime.strptime(real, '%H:%M')

        estimated_duration_td = timedelta(hours=estimated_dt.hour, minutes=estimated_dt.minute)
        realtime_duration_td = timedelta(hours=realtime_dt.hour, minutes=realtime_dt.minute)

        diff_td = realtime_duration_td - estimated_duration_td
        seconds = diff_td.seconds
        calc = f"{int(seconds / 3600)}"+f': {(int(seconds / 60)) % 60} '
        correctness = 100 * realtime_duration_td.seconds / estimated_duration_td.seconds

        # saving data in task
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
        return redirect(reverse('home'))

"""

# Or this method (2)
class TaskView(TemplateView):
    template_name = 'tracker/home.html'
    # get: displays the page and the data therein
    def get(self, request):
        data = Task.objects.all()
        form = CreateTaskForm()
        # averaging
        total_correctness = 0
        liste = []
        for _data in data:
            liste.append(_data.correctness)
        for x in liste:
            total_correctness = x + total_correctness

        moyenne_correctness = round(total_correctness / len(liste), 3)

        context = {'data':data, 'form':form, 'moyenne_correctness': moyenne_correctness}
        return render (request,self.template_name, context)

    # post: retrieves the form data to save and reload the home page
    def post(self, request):
        form = CreateTaskForm(request.POST)
        form.save()
        return redirect(reverse('home'))
