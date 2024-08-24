from rest_framework import routers
from .views import VehicleViewSet
from django.urls import path
from .views import *

router = routers.DefaultRouter()
router.register('', VehicleViewSet)

urlpatterns =[
    path('create/', createView, name='criar-veiculo'),
    
    path('list/', listView, name='listar-veiculos'),

    path('update/<int:id>', updateView, name='atualizar-veiculo'),

    path('delete/<int:id>', deleteView, name='deletar-veiculo'),
]

urlpatterns += router.urls
