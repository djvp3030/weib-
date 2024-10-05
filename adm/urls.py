from django.urls import path, include
from . import views

urlpatterns = [
  path('main/', views.main_sm, name= 'Sm_main' ),
  path('añadir_servicios', views.añadir_servicios, name= 'Aservices'),
  path('añadir_users',views.añadir_usuarios, name='Ausers'),
  path('ver_servicos',views.ver_servicios, name='Vs'),
  path('ver_usuarios',views.ver_users, name='Vu'),
  path('ver_productos',views.ver_tienda, name='Vt'),
  path('editar_users/<int:id>/', views.editar_user, name='EditU'),
  path('editar_productos/<int:id>/', views.editar_tienda, name='EditT'),
  path('editar_servicios/<int:id>/', views.editar_servicios, name='EditS'),
  path('delete_users/<int:id>/', views.delete_user, name='DeleteU'),
  path('delete_servicios/<int:id>/', views.delete_servicios, name='DeleteS'),
  path('delete_productos/<int:id>/', views.delete_productos, name='DeleteT'),
  path('delete_size/<int:id>/', views.delete_size, name='DeleteSZ'),
  path('añadir_productos', views.añadir_productos, name='Aprod'),
  path('añadir_sized', views.añadir_size, name='Asize'),
  path('servicios_solicitados', views.servicicos_sol, name='servicesSol'),
  path('productos_comprados', views.productos_comp, name='productosComp')
  

] 
