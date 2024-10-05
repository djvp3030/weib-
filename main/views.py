from django.shortcuts import render
from adm.models import servicios, producto

# Create your views here.

def main(request): 
  Servicios = servicios.objects.order_by('?')[:2]
  tienda =  producto.objects.order_by('?')[:2]
  return render(request,'main.html',{'services':Servicios, 'tienda':tienda})
  

