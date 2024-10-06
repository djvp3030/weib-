from django.db import models

class servicios(models.Model):
  nombre = models.CharField(max_length= 100)
  descripcion = models.TextField()
  img_prev = models.ImageField(upload_to= 'servicios', null=True)
  img_comp = models.ImageField(upload_to= 'servicios', null=True)
  
class producto(models.Model):
  nombre = models.CharField(max_length=100)
  descripcion = models.TextField()
  img_prev = models.ImageField(upload_to='tienda', null=True)
  img_comp = models.ImageField(upload_to='tienda', null=True)
  
  def __str__(self):
      return self.nombre
  
class size(models.Model):
  product = models.ForeignKey('producto', on_delete=models.CASCADE, blank=False, null=False, related_name='Tamaño')
  tamaño = models.CharField(max_length=10, null=True, blank=True)
  
  def __str__(self):
     return self.tamaño