from django.shortcuts import render,redirect
from .models import * 
from .forms import * 

# Create your views here.
# This method (1)
def home(request):
    if request.method == "POST":
        name = request.POST['name']
        planning = request.POST['planning']
        estimated = request.POST['estimated']
        real = request.POST['real']
        risk = request.POST['risk']
        level = request.POST['level']
        notes = request.POST['notes']
        
        table = Table(name=name,
        planning=planning,
        estimate=estimated,
        realtime=real,
        risk=risk,
        level=level,
        notes=notes,
        )
        table.save()
    data = Table.objects.all()
    context = {'data':data}
    return render (request,'tracker/home.html', context)
    
# Or this (2)
"""
def home(request):
    form = DataForm()
    if request.method == "POST":
        form = DataForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')

    data = Table.objects.all()
    context = {'data':data,'form':form}
    return render (request,'tracker/home.html', context)

"""