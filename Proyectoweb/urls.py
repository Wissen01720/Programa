from django.urls import path

from Proyectoweb import views

urlpatterns = [
    path('', views.index, name="Index"),
    path('Circuitos/', views.mecanic, name="Circuitos"),
    path('Electromagnetismo/', views.electromagnetismo, name="Electromagnetismo"),
    path('Calculadora/', views.calculadora, name="Calculadora"),
]
