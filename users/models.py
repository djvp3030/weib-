from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.core.validators import RegexValidator


# Create your models here.
class rangos(BaseUserManager):
  
  def create_user(self,email,first_name,last_name,telefono,username, password = None):
    
    if not email:
      raise ValueError('Ingrese email')
    
    user = self.model(username = username , email = self.normalize_email(email), last_name = last_name, first_name = first_name, telefono = telefono )
    
    user.set_password(password)
    user.save()
    return user
    
  def create_superuser(self,first_name,last_name,email,telefono,username, password):
    superu = self.create_user(email, username = username , last_name = last_name, first_name = first_name, telefono = telefono, password=password)
    
    superu.is_admin = True
    superu.staff = True
    superu.save()
    return superu
  
  def create_staffuser(self,first_name,last_name,email,telefono,username, password):
    Staff = self.create_user(email, username = username , last_name = last_name, first_name = first_name, telefono = telefono, password=password)
    
    Staff.staff = True
    Staff.save()
    return Staff

class User(AbstractBaseUser):  
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  email = models.EmailField(max_length=254, unique=True)
  telefono = models.CharField(max_length= 11, validators=[RegexValidator(r'^\d{1,10}$')])
  username = models.CharField(max_length=20, unique=True,)
  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False )
  staff = models.BooleanField(default=False )
  objects = rangos()
  
  USERNAME_FIELD = 'username'
  REQUIRED_FIELDS = ['first_name','last_name','email','telefono']
  
  def __str__(self):
    return f'{self.first_name} {self.last_name}'

  def has_perm(self,perm,obj = None) :
    return True	
  
  def has_module_perms(self,app_label):
    return True
  
  @property
  def is_staff(self):
    return self.is_admin
  