from django.urls import path
from . import views

urlpatterns = [
    path('equipo/', views.vista_equipo, name='equipo'),
    path('servicio-tecnico/', views.vista_servicio_tecnico, name='servicio_tecnico'),
    path('tecnicos/', views.vista_tecnicos, name='tecnicos'),
]

