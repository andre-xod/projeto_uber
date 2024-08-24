from django.db import models
from vehicle.models import Vehicle

class Driver(models.Model):
    nome = models.CharField(verbose_name='Nome do motorista', max_length=150)
    cpf = models.CharField(verbose_name='Cpf do motorista', max_length=11)
    telefone = models.CharField(verbose_name='Telefone do motorista', max_length=11)
    habilitacao = models.CharField(verbose_name='Habilitação do motorista', max_length=9)

    veiculo = models.OneToOneField(Vehicle, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.nome
