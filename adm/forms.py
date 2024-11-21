from django import forms
from .models import servicios, producto, size
from users.models import User
from django.contrib.auth.forms import UserCreationForm

class services(forms.ModelForm):
  
  class Meta:
    model = servicios
    
    fields = [
      'nombre', 'descripcion', 'img_prev' , 'img_comp'
    ]
    labels = {
      'nombre':'Nombre',
      'descripcion': 'Descripcion',
      'img_prev':'Imagen 1',
      'img_comp':'Imagen 2',
    }
    
    widgets = {
      'nombre':forms.TextInput(attrs={'class':'shadow duration-200 hover:scale-110 focus:shadow-md rounded-md ml-2'}),
      'descripcion':forms.Textarea(attrs={'class':'shadow duration-200 hover:scale-105 focus:shadow-md rounded-md  ml-2'}),
      'img_prev':forms.FileInput(attrs={'class':'shadow duration-200 hover:scale-105 focus:shadow-md rounded-md ml-2'}),
      'img_comp':forms.FileInput(attrs={'class':'shadow duration-200 hover:scale-105 focus:shadow-md rounded-md ml-2'})
    }
    
class usuarios(UserCreationForm):
  
  password1 = forms.CharField(label="Contraseña",widget=forms.PasswordInput(attrs={'class':'shadow duration-200 hover:scale-110 focus:shadow-md rounded-md ml-4 w-80', 'id':'password1'}))
  password2 = forms.CharField(label="Confirmar Contraseña",widget=forms.PasswordInput(attrs={'class':'shadow duration-200 hover:scale-110 focus:shadow-md rounded-md ml-4 w-64','id':'password2'}))
  
  class Meta:
      model= User
      
      fields=['first_name','last_name','email','telefono','username','is_admin','staff',]
      
      labels = {
        'first_name':'Nombres',
        'last_name':'Apellidos',
        'email':'Correo electronico',
        'telefono':'Numero Telefonico',
        'username':'Nombre de usuario',
        'is_admin':'¿Administrador?',
        'staff':'¿moderador?',
      }
      
      widgets = {
        'first_name':forms.TextInput(attrs={'class':'shadow duration-200 hover:scale-110 focus:shadow-md rounded-md   ml-4 w-80'}),
        'last_name': forms.TextInput(attrs={'class':'shadow duration-200 hover:scale-110 focus:shadow-md rounded-md ml-4 w-80'}),
        'email': forms.EmailInput(attrs={'class':'shadow duration-200 hover:scale-110 focus:shadow-md rounded-md ml-4 w-64'}),
        'telefono': forms.TextInput(attrs={'class':'shadow duration-200 hover:scale-110 focus:shadow-md rounded-md ml-4 w-64'}),
        'username':forms.TextInput(attrs={'class':'shadow duration-200 hover:scale-110 focus:shadow-md rounded-md ml-4 w-64'}),
      }
      
      

class productos(forms.ModelForm):
    class Meta:
      model= producto
      fields = ['nombre','descripcion','img_prev', 'img_comp']
      
      labels = {
        'nombre': 'nombre',
        'descripcion': 'descripcion',
        'img_prev':'imagen 1',
        'img_comp':'imagen 2'
      }
      
      widgets = {
        'nombre':forms.TextInput(attrs={'class':'shadow duration-200 hover:scale-110 focus:shadow-md rounded-md ml-2'}),
        'descripcion':forms.Textarea(attrs={'class':'shadow duration-200 hover:scale-105 focus:shadow-md rounded-md  ml-2'}),
        'img_prev':forms.FileInput(attrs={'class':'shadow duration-200 hover:scale-105 focus:shadow-md rounded-md ml-2'}),
        'img_comp':forms.FileInput(attrs={'class':'shadow duration-200 hover:scale-105 focus:shadow-md rounded-md ml-2'})
      }
      
      
class Size(forms.ModelForm):
   class Meta:
     model = size
     fields = ['tamaño','product','id']
    
     labels = {
       'tamaño': 'tamaño',
       'product': 'producto'
     }
    
     widgets = {
      'tamaño': forms.TextInput(attrs={'class':'shadow duration-200 hover:scale-105 focus:shadow-md rounded-md ml-2'}),
      'product': forms.Select(attrs={'class':'shadow duration-200 hover:scale-105 focus:shadow-md rounded-md ml-2'})
    }


class editar_users(forms.ModelForm):
  class Meta:
    model = User
    fields=['first_name','last_name','email','telefono','username','is_admin','staff',]

      
    widgets = {
      'first_name':forms.TextInput(attrs={'class':'shadow duration-200 hover:scale-110 focus:shadow-md rounded-md   ml-2'}),
      'last_name': forms.TextInput(attrs={'class':'shadow duration-200 hover:scale-110 focus:shadow-md rounded-md ml-2'}),
      'email': forms.EmailInput(attrs={'class':'shadow duration-200 hover:scale-110 focus:shadow-md rounded-md ml-2'}),
      'telefono': forms.TextInput(attrs={'class':'shadow duration-200 hover:scale-110 focus:shadow-md rounded-md mr-8'}),
      'username':forms.TextInput(attrs={'class':'shadow duration-200 hover:scale-110 focus:shadow-md rounded-md mr-8'}),
    }