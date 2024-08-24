from rest_framework import viewsets
from .serializers import DriverSerializer
from django.shortcuts import render, redirect
from .models import Driver
from .forms import DriverForm
from django.shortcuts import get_object_or_404

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer 

def createView(request):
    context={}
    form = DriverForm()

    if request.method == 'POST':
        form = DriverForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('listar-motoristas')

    context['form'] = form
    return render(request, 'create-driver.html', context)

def listView(request):
    context={}
    drivers = Driver.objects.all()

    context['drivers'] = drivers
    return render(request, 'list-driver.html', context)

def updateView(request, id):
    context={}
    driver = get_object_or_404(Driver, pk = id)
    form = DriverForm(request.POST or None, instance=driver)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('listar-motoristas')

    context['form'] = form
    return render(request, 'update-driver.html', context)

def deleteView(request, id):
    context={}
    driver = get_object_or_404(Driver, pk = id)
    driver.delete()

    return redirect('listar-motoristas')
