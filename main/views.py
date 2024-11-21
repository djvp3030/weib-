from django.shortcuts import render
from adm.models import servicios, producto
import os 
from django.conf import settings
from random import shuffle

  
def main(request): 
  Servicios = servicios.objects.order_by('?')[:2]
  tienda =  producto.objects.order_by('?')[:2]
  
  image_dir_carrusel = os.path.join(settings.BASE_DIR, 'staticfiles', 'carrusel')
  images_carrusel = [f for f in os.listdir(image_dir_carrusel) if f.endswith(('webp'))]
  shuffle(images_carrusel)
  
  image_dir_productos = os.path.join(settings.BASE_DIR, 'staticfiles', 'productos')
  images_productos = [f for f in os.listdir(image_dir_productos) if f.endswith(('webp'))]
  shuffle(images_productos)
  
  image_dir_servicios = os.path.join(settings.BASE_DIR, 'staticfiles', 'servicios')
  images_servicios = [f for f in os.listdir(image_dir_servicios) if f.endswith(('webp'))]
  shuffle(images_servicios)
  
  return render(request,'main.html',{'services':Servicios, 'tienda':tienda,'imgs_c': images_carrusel, 'imgs_servicios':images_servicios, 'imgs_productos':images_productos})
  

