from rest_framework import viewsets
from .serializers import VehicleSerializer
from django.shortcuts import render, redirect
from .models import Vehicle
from .forms import VehicleForm
from django.shortcuts import get_object_or_404

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

def createView(request):
    context={}
    form = VehicleForm()

    if request.method == 'POST':
        form = VehicleForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('listar-veiculos')
        
    context['form'] = form
    return render(request, 'create-vehicle.html', context)

def listView(request):
    context={}
    vehicles = Vehicle.objects.all()

    context['vehicles'] = vehicles
    return render(request, 'list-vehicle.html', context)

def updateView(request, id):
    context={}
    vehicle = get_object_or_404(Vehicle, pk = id)
    form = VehicleForm(request.POST or None, instance=vehicle)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('listar-veiculos')
        
    context['form'] = form
    return render(request, 'update-vehicle.html', context)

def deleteView(request, id):
    context={}
    vehicle = get_object_or_404(Vehicle, pk = id)
    vehicle.delete()

    return redirect('listar-veiculos')
