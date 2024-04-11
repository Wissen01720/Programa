from django.urls import path

from Proyectoweb import views

urlpatterns = [
    path('', views.index, name="Index"),
    path('Mecanica/', views.mecanic, name="Mecanica"),
    path('Electromagnetismo/', views.electromagnetismo, name="Electromagnetismo"),
    path('Calculadora/', views.calculadora, name="Calculadora"),
]
