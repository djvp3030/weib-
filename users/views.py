from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import get_user_model
from .models import User
from adm.forms import usuarios,editar_users
from django.contrib import messages
from services_store.models import factura_servicios,factura_tienda
# Create your views here.

def register(request): 
  if request.method == 'POST':
    form = usuarios(request.POST)
    del form.fields['is_admin']
    del form.fields['staff']
    if form.is_valid():
      try:
          usr = form.save()
          login(request,usr)
          messages.success(request, 'registro realizado exitosamente ')
          return redirect('main')
      except Exception as e:
        messages.error(request, f'Ocurrió un error: {str(e)}')
    else:
      error = form.errors
      for field in form:
          for error in field.errors:
              messages.error(request, f'Error en {field.label}: {error}')
      
  else:
    form = usuarios()
    del form.fields['is_admin']
    del form.fields['staff']

  return render(request,'register.html',{'form':form})
    
def Login(request):
  global User
  user = get_user_model()
  error = False
  if request.method == 'GET':
    return render(request, 'loggin.html')
  else:
    print(request.POST)
    username = request.POST['name']
    password = request.POST['password']
    try:
      error = False
      usr = User.objects.get(username=username)
    except:
      error = True
      return render(request, 'loggin.html', {'error':'Nombre de usuario no existe', 'Error':error})
    
    usr = authenticate(request, username=username, password=password)
    if usr is None:
      error = True
      return render(request, 'loggin.html', {'error':'Nombre de usuario o password es incorrecto intente de nuevo', 'Error':error})
    else:
      error = False 
      login(request,usr)
      messages.success(request, f'bienvenido {username}  ')
      return redirect('/main')


def singout(request):
  logout(request)
  messages.success(request, 'hasta luego ')
  return redirect('main/')

  
@login_required
def ver_userN(request,id):
  user = User.objects.get(pk = id)
  if request.method == 'GET':
    form = editar_users(instance= user)
    form.fields.pop('staff')
    form.fields.pop('is_admin')
    return render(request, 'ver_userN.html', {'form':form} )
  else:
    form = editar_users(request.POST,instance=user)
    if form.is_valid():
      form.save()
      messages.success(request, 'usuario editado exitosamente ')
    return redirect('main')

@login_required
def delete_user_normal(request,id):
    user = User.objects.get(pk = id)
    user.delete()
    messages.success(request, 'Usuario eliminado correctamente ')
    return redirect('main')
  

@login_required
def servicicos_solicitados(request,id):
  servicios = factura_servicios.objects.filter(solicitante = id)
  return render(request, 'servicios_sol.html', {'servicio':servicios})

@login_required
def historial_compra(request, id ):
  productos = factura_tienda.objects.filter(solicitante = id)
  return render(request, 'historial_comp.html', {'productos':productos})