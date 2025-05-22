from django.db import models
class Paquete(models.Model):
    destino = models.CharField(max_length=100)
precio_diario = models.IntegerField()
def __str__(self):
    return self.destino