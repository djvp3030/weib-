from django.urls import path, include
from . import views

urlpatterns = [
  path('servicios/',views.Servicios, name= 'servicios'),
  path('compra_servicos/<int:id>',views.compra_s, name='compS'),
  path('tienda/',views.tienda, name= 'tienda'),
  path('tienda_compra/<int:id>',views.compra_t, name= 'tiendaC'),
] 