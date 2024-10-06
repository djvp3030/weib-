from django.db import models
from users.models import User

class factura_servicios(models.Model):
  pd = 'pendiente'
  np = 'en proceso'
  fn = 'finalizado'
  elecciones = [
    (pd , 'pendiente'),(np, 'en proceso'),(fn, 'finalizado')
    ]
  solicitante = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
  telefono = models.CharField(max_length=100)
  servicio = models.CharField(max_length=100)
  fechaDeCita = models.DateField()
  direccion = models.CharField(max_length=100)
  fechaSolicitada = models.DateTimeField(auto_now_add=True)
  estado = models.CharField(max_length=100,choices = elecciones , default = np)
  fechaFinalizado = models.DateField(blank= True, null=True)
  
class factura_tienda(models.Model):
  solicitante = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
  producto = models.CharField(max_length=100)
  tamaño = models.CharField(max_length=100)
  fechaCompra = models.DateTimeField(auto_now_add=True)
  