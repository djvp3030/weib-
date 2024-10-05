from django.shortcuts import render
from adm.models import servicios, producto, size
from users.models import User
from .models import factura_tienda , factura_servicios
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required
def Servicios(request):
  servicio = servicios.objects.all()
  print(servicio)
  return render(request, 'servicios.html', {'servicio':servicio})

@login_required
def compra_s(request,id):
  service = servicios.objects.get(pk=id)
  user = request.POST.get('id_user')
  if request.method =="GET":
      return render(request, 'comprar_services.html', {'service':service})
  else:
    user_instace = User.objects.get(pk = user)
    compra = factura_servicios.objects.create(solicitante = user_instace, fechaDeCita= request.POST['fecha-de-cita'], telefono = request.POST['telefono'], servicio = request.POST['servicio'], direccion= request.POST['direccion'])
    compra.save()
    messages.success(request, 'servicio solicitado exitosamente')
    return render(request, 'main.html')
  

@login_required
def tienda(request):
  tienda = producto.objects.all()
  return render(request, 'tienda.html', {'tienda':tienda})

@login_required
def compra_t(request,id):
  tienda = producto.objects.get(pk=id)
  user = request.POST.get('id_user')
  if request.method =="GET":
      size = tienda.Tamaño.all()
      return render(request, 'comprar_tienda.html', {'tienda':tienda, 'size':size})
    
  else:
    user_instace = User.objects.get(pk = user)
    compra = factura_tienda.objects.create(solicitante = user_instace, producto = request.POST['producto'], tamaño = request.POST['tamaño'], precio = request.POST['precio'], metodo_pago = request.POST['metodo de pago'])
    compra.save()
    messages.success(request, 'producto comprado exitosamente')
    return render(request, 'main.html')
