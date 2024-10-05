from django.shortcuts import render,redirect, get_object_or_404
from .forms import services,usuarios,productos, Size, editar_users
from users.models import User 
from .models import servicios,producto, size
from django.contrib.auth.decorators import login_required, user_passes_test
from PIL import Image, ImageOps
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys 
from services_store.models import factura_servicios,factura_tienda
from django.contrib import messages


def admin(user):
  return user.is_authenticated and user.is_admin
def Staff(user):
  return user.is_authenticated and user.staff

@login_required
@user_passes_test(Staff)
def main_sm(request):
  return render(request,'main_ms.html', )

@login_required
@user_passes_test(admin)
def añadir_servicios(request): 
  if request.method == "POST":
    form = services(request.POST, files=request.FILES)
    if form.is_valid():
        servicios = form.save(commit=False)
        
        img_prev = request.FILES['img_prev']
        img_comp = request.FILES['img_comp']
        
        img = Image.open(img_prev) 
        img2 = Image.open(img_comp)
        img = ImageOps.exif_transpose(img)
        img2 = ImageOps.exif_transpose(img2)
        img = img.resize((500, 500))
        img2 = ImageOps.exif_transpose(img2)
        img_io = BytesIO()
        img_io2 = BytesIO()
        img.save(img_io, format='WEBP')
        img2.save(img_io2, format='WEBP')
        img_file = InMemoryUploadedFile(img_io,'ÍmageField', f'{img_prev.name}.webp','image/webp',sys.getsizeof(img_io), None)
        img_file2 = InMemoryUploadedFile(img_io2,'ÍmageField', f'{img_comp.name}.webp','image/webp',sys.getsizeof(img_io2), None)
        
        servicios.img_prev = img_file
        servicios.img_comp = img_file2
        
        messages.success(request, 'servicio creado exitosamente ')
        servicios.save()
        
        return redirect('Sm_main')
  else:
    form = services()
    
  return render(request,'añadir_servicios.html', {'form':form})

@login_required
@user_passes_test(admin)
def añadir_productos(request): 
  if request.method == "POST":
    form = productos(request.POST, files=request.FILES)
    if form.is_valid():
        producto = form.save(commit=False)
        
        img_prev = request.FILES['img_prev']
        img_comp = request.FILES['img_comp']
        
        img = Image.open(img_prev) 
        img2 = Image.open(img_comp)
        img = ImageOps.exif_transpose(img)
        img2 = ImageOps.exif_transpose(img2)
        img = img.resize((500, 500))
        img2 = ImageOps.exif_transpose(img2)
        img_io = BytesIO()
        img_io2 = BytesIO()
        img.save(img_io, format='WEBP')
        img2.save(img_io2, format='WEBP')
        img_file = InMemoryUploadedFile(img_io,'ÍmageField', f'{img_prev.name}.webp','image/webp',sys.getsizeof(img_io), None)
        img_file2 = InMemoryUploadedFile(img_io2,'ÍmageField', f'{img_comp.name}.webp','image/webp',sys.getsizeof(img_io2), None)
        
        producto.img_prev = img_file
        producto.img_comp = img_file2
        producto.save()
        
        messages.success(request, 'Producto creado exitosamente ')
        return redirect('Sm_main')
  else:
    form = productos
    return render(request,'añadir_productos.html', {'form':form})

@login_required
@user_passes_test(admin)
def añadir_size(request):
  if request.method == 'POST':
    form = Size(request.POST)
    if form.is_valid():
      form.save()

      messages.success(request, 'tamaño creado exitosamente ')
      return redirect('Sm_main')
  else:
    form = Size
    productos = producto.objects.all() 
    return render(request,'añadir_tamaño.html', {'form':form, 'producto':productos})

@login_required
@user_passes_test(admin)
def añadir_usuarios(request):
  if request.method == 'POST':
    form = usuarios(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'usuario creado exitosamente ')
      return redirect('Sm_main')
  else:
    form = usuarios()
  
  return render(request,'añadir_users.html',{'form':form})

@login_required
@user_passes_test(Staff)
def ver_servicios(request):
  servicio = servicios.objects.all()
  return render(request, 'ver_s.html', {'servicio':servicio})

@login_required
@user_passes_test(Staff)
def ver_users(request):
  users = User.objects.all()
  return render(request,'ver_u.html', {'users':users})

@login_required
@user_passes_test(Staff)
def ver_tienda(request):
  tienda = producto.objects.all()
  return render(request, 'ver_t.html', {'tienda':tienda})

@login_required
@user_passes_test(Staff)
def editar_user(request,id):
  user = User.objects.get(pk = id)
  if request.method == 'GET':
    form = editar_users(instance=user)
    if user.is_admin == False:
      del form.fields['is_admin']
    return render(request, 'editar_user.html', {'form':form})
  else:
    form = editar_users(request.POST,instance=user)
    print(form)
    if form.is_valid():
      form.save()
      messages.success(request, 'usuario editado exitosamente ')
    return redirect('Sm_main')
  

@login_required
@user_passes_test(Staff)  
def editar_servicios(request,id):
  if request.method == 'GET':
    service = servicios.objects.get(pk = id)
    form = services(instance=service)
    return render(request,'editar_servicios.html', {'form':form})
  else:
    service = servicios.objects.get(pk = id)
    form = services(request.POST,instance=service)
    form.save()
    messages.success(request, 'servicio editado exitosamente ')
    return redirect('Sm_main')
  
@login_required
@user_passes_test(Staff)  
def editar_tienda(request,id):
  tienda = get_object_or_404(producto, pk = id)
  tamaño = tienda.Tamaño.all()
  if request.method == 'GET':
    form = productos(instance = tienda)
    form2 = Size(request.POST)
    return render(request,'editar_tienda.html', {'form':form, 'tamaño':tamaño, 'form2':form2})
  else:
    form2 = Size(request.POST)
    size_id = request.POST.get('size_id')
    if size_id:
            tamaño = get_object_or_404(size, pk=size_id)
            form2 = Size(request.POST, instance=tamaño)
            if form2.is_valid():
                form2.save()
                messages.success(request, 'tamaño editado exitosamente ')
                return redirect('Sm_main')
    tienda = producto.objects.get(pk = id)
    form = productos(request.POST,instance=tienda)
    if form.is_valid():
      form.save()
      messages.success(request, 'producto editado exitosamente ')
      return redirect('Sm_main')

@login_required
@user_passes_test(admin)  
def delete_user(request,id):
  user = User.objects.get(pk = id)
  user.delete()
  messages.success(request, 'usuario eliminado exitosamente ')
  return redirect('Sm_main')

@login_required
@user_passes_test(admin)  
def delete_servicios(request,id):
  service = servicios.objects.get(pk = id)
  service.delete()
  messages.success(request, 'servicio eliminado exitosamente ')
  return redirect('Sm_main')

@login_required
@user_passes_test(admin)  
def delete_productos(request,id):
  productos = producto.objects.get(pk = id)
  productos.delete()
  messages.success(request, 'producto eliminado exitosamente ')
  return redirect('Sm_main')

@login_required
@user_passes_test(admin)  
def delete_size(request,id):
  tamaño = size.objects.get(pk = id)
  tamaño.delete()
  messages.success(request, 'tamaño eliminado exitosamente ')
  return redirect('Sm_main')


@user_passes_test(Staff)
def servicicos_sol(request):
  servicios = factura_servicios.objects.all()
  if request.method == 'GET':
    return render(request, 'servicios_solicitados.html', {'servicio':servicios})
  else:
    estado = request.POST.get('estado')
    id_factura = request.POST.get('id_factura')
    fecha_finalizacion = request.POST.get('fecha_finalizacion')
    servicios = factura_servicios.objects.get(pk = id_factura)
    servicios.estado = estado
    servicios.fechaFinalizado = fecha_finalizacion
    servicios.save()
    messages.success(request, 'factura actualizada exitosamente ')
    return redirect('Sm_main')

@user_passes_test(Staff)
def productos_comp(request):
  productos = factura_tienda.objects.all()
  if request.method == 'GET':
    return render(request, 'productos_comprados.html', {'productos':productos})
  else:
    pago = request.POST.get('pago')
    id_producto = request.POST.get('id_producto')
    productos = factura_tienda.objects.get(pk = id_producto)
    productos.pago = pago
    productos.save()
    messages.success(request, 'factura actualizada exitosamente ')
    return redirect('Sm_main')