from django.db import models

class Vehicle(models.Model):
    marca = models.CharField(verbose_name='Marca do carro', max_length=50)
    placa = models.CharField(verbose_name='Placa do carro', max_length=7)
    cor = models.CharField(verbose_name='Cor do carro', max_length=50)
    modelo = models.CharField(verbose_name='Modelo do carro', max_length=50)
    qtdPassageiros = models.IntegerField(verbose_name= 'Quantidade de passageiros')

    def __str__(self) -> str:
        return self.marca + ' ' + self.modelo + ' ' + self.cor
