from django.shortcuts import render, HttpResponse
from . import calculations


# Create your views here.


def index(request):
    return render(request, "Proyectoweb/Index.html")


def mecanic(request):
    return render(request, "Proyectoweb/Circuitos.html")


def electromagnetismo(request):
    return render(request, "Proyectoweb/Electromagnetismo.html")


def calculadora(request):
    return render(request, "Proyectoweb/Calculadora.html")

def calcular(request):
    if request.method == 'POST':
        calculo = request.POST.get('calculo')
        if calculo == 'energia_cinetica':
            masa = float(request.POST.get('masa'))
            velocidad = float(request.POST.get('velocidad'))
            resultado = calculations.calcular_energia_cinetica(masa, velocidad)
        elif calculo == 'energia_potencial':
            masa = float(request.POST.get('masa'))
            altura = float(request.POST.get('altura'))
            resultado = calculations.calcular_energia_potencial(masa, altura)
        elif calculo == 'energia_mecanica':
            energia_cinetica = float(request.POST.get('energia_cinetica'))
            energia_potencial = float(request.POST.get('energia_potencial'))
            resultado = calculations.calcular_energia_mecanica(energia_cinetica, energia_potencial)
        elif calculo == 'trabajo':
            fuerza = float(request.POST.get('fuerza'))
            distancia = float(request.POST.get('distancia'))
            angulo = float(request.POST.get('angulo'))
            resultado = calculations.calcular_trabajo(fuerza, distancia, angulo)
        elif calculo == 'caida_libre':
            altura = float(request.POST.get('altura'))
            resultado = calculations.calcular_caida_libre(altura)
        elif calculo == 'velocidad_final':
            velocidad_inicial = float(request.POST.get('velocidad_inicial'))
            aceleracion = float(request.POST.get('aceleracion'))
            tiempo = float(request.POST.get('tiempo'))
            resultado = calculations.calcular_velocidad_final(velocidad_inicial, aceleracion, tiempo)
        elif calculo == 'altura_maxima':
            velocidad_inicial = float(request.POST.get('velocidad_inicial'))
            aceleracion = float(request.POST.get('aceleracion'))
            resultado = calculations.calcular_altura_maxima(velocidad_inicial, aceleracion)
        elif calculo == 'distancia_recorrida':
            velocidad_inicial = float(request.POST.get('velocidad_inicial'))
            tiempo = float(request.POST.get('tiempo'))
            aceleracion = float(request.POST.get('aceleracion'))
            resultado = calculations.calcular_distancia_recorrida(velocidad_inicial, tiempo, aceleracion)
        elif calculo == 'fuerza':
            masa = float(request.POST.get('masa'))
            aceleracion = float(request.POST.get('aceleracion'))
            resultado = calculations.calcular_fuerza(masa, aceleracion)
        elif calculo == 'aceleracion':
            fuerza = float(request.POST.get('fuerza'))
            masa = float(request.POST.get('masa'))
            resultado = calculations.calcular_aceleracion(fuerza, masa)
        elif calculo == 'masa':
            fuerza = float(request.POST.get('fuerza'))
            aceleracion = float(request.POST.get('aceleracion'))
            resultado = calculations.calcular_masa(fuerza, aceleracion)
        elif calculo == 'fuerza_elastica':
            constante_resorte = float(request.POST.get('constante_resorte'))
            deformacion = float(request.POST.get('deformacion'))
            resultado = calculations.calcular_fuerza_elastica(constante_resorte, deformacion)
        elif calculo == 'constante_resorte':
            fuerza_elastica = float(request.POST.get('fuerza_elastica'))
            deformacion = float(request.POST.get('deformacion'))
            resultado = calculations.calcular_constante_resorte(fuerza_elastica, deformacion)

        return render(request, 'calculadora.html', {'resultado': resultado})
    else:
        resultado = 'No se ha enviado ningún formulario'