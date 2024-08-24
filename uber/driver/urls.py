from rest_framework import routers
from .views import DriverViewSet
from django.urls import path
from .views import *

router = routers.DefaultRouter()
router.register('', DriverViewSet)

urlpatterns = [
    path('create/', createView, name='criar-motorista'),

    path('list/', listView, name='listar-motoristas'),

    path('update/<int:id>', updateView, name='atualizar-motorista'),

    path('delete/<int:id>', deleteView, name='deletar-motorista'),
    
]

urlpatterns += router.urls
