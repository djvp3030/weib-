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
  tf = 'transferencia'
  pm = 'pago movil'
  ef = 'efectivo'
  elecciones = [
    (tf, 'transferencia'),(pm, 'pago movil'),(ef, 'transferencia')
  ]
  solicitante = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
  producto = models.CharField(max_length=100)
  tamaño = models.CharField(max_length=20)
  precio = models.DecimalField(max_digits=10, decimal_places=2)
  fechaCompra = models.DateTimeField(auto_now_add=True)
  metodo_pago = models.CharField(max_length=100,choices =elecciones, default=ef)
  pago = models.BooleanField(default= False)