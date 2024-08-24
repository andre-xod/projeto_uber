from django.shortcuts import render
from vehicle.models import Vehicle

def homeView(request):
    context = {}
    veiculos = Vehicle.objects.all()

    context['veiculos'] = veiculos
    return render(request, 'index.html', context)
