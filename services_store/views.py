from django.shortcuts import render
from adm.models import servicios, producto, size
from users.models import User
from .models import factura_tienda , factura_servicios
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
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
    user_email = request.POST.get('correo')
    user_phone = request.POST.get('telefono')
    name = request.POST.get('name')
    compra = factura_servicios.objects.create(solicitante = user_instace, fechaDeCita= request.POST['fecha-de-cita'], telefono = request.POST['telefono'], servicio = request.POST['servicio'], direccion= request.POST['direccion'])
    compra.save()
    messages.success(request, 'servicio solicitado exitosamente')
    
    
    subject = 'una solicitud de servicio ha sido realizada'
    
    message = f'''el usuario {name} ha realizado una peticion del servicio {request.POST['servicio']}. 
    
    Direccion: {request.POST['direccion']}
    
    Fecha de solicitud: {request.POST['fecha-de-cita']}
    
    Correo del cliente : {user_email}
    
    telefono del cliente: {user_phone}
    '''
    
    try:
      send_mail(
        subject,message,
        settings.EMAIL_HOST_USER,
        ['Weibservicios@gmail.com'],
        fail_silently=False,
      )
    
    except Exception as e:
      
      print(f'Error al enviar el correo: {e}')

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
    user_email = request.POST.get('correo')
    user_phone = request.POST.get('telefono')
    name = request.POST.get('name')
    compra = factura_tienda.objects.create(solicitante = user_instace, producto = request.POST['producto'], tamaño = request.POST['cantidad'],)
    compra.save()
    messages.success(request, 'producto comprado exitosamente')
    
    
    subject = 'una solicitud de servicio ha sido realizada'
    message = f'''el usuario {name} ha realizado una peticion del servicio {request.POST['producto']}. 
    
    Correo del cliente : {user_email}
    
    telefono del cliente: {user_phone}
    '''
    try:
      send_mail(
        subject,message,
        settings.EMAIL_HOST_USER,
        ['Weibca@gmail.com'],
        fail_silently=False,
      )
    except Exception as e:
      print(f'Error al enviar el correo: {e}')
      
    return render(request, 'main.html')
