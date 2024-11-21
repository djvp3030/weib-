from django.urls import path, include
from . import views


urlpatterns = [
  path('register/', views.register, name = 'register'),
  path('loggin/', views.Login, name = 'loggin'),
  path('ver_userN/<int:id>', views.ver_userN, name='verUN'),
  path('delete_user/<int:id>/', views.delete_user_normal, name='EliminarU'),
  path('historial_copm_servicios/<int:id>', views.servicicos_solicitados, name='historial_comp_servicios'),
  path('historial_copmra/<int:id>', views.historial_compra, name='historial_compra')
]