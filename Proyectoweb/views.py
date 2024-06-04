from django.shortcuts import render
from . import calculations  # Asegúrate de que 'calculations' esté en el mismo directorio que 'views.py'

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
        funciones_calculo = {
            'resistencia_serie': calculations.calcular_resistencias_circuitoSerie,
            'resistencia_paralelo': calculations.calcular_resistencias_circuitoParalelo,
            'resistencia_mixto': calculations.calcular_resistencia_circuitoMixto
        }
        try:
            resistencias = []
            for i in range(1, 6):
                resistencia = request.POST.get(f'resistencia{i}')
                if resistencia:
                    resistencias.append(float(resistencia))

            if calculo == 'resistencia_mixto':
                resistencias_serie = resistencias[:2]
                resistencias_paralelo = resistencias[2:]
                if len(resistencias_serie) < 2 or len(resistencias_paralelo) < 1:
                    raise ValueError('Faltan valores de resistencia para el cálculo.')
                resistencias = [resistencias_serie, resistencias_paralelo]
            else:
                if len(resistencias) < 2:
                    raise ValueError('Faltan valores de resistencia para el cálculo.')

            resultado = funciones_calculo[calculo](resistencias)
            return render(request, 'Proyectoweb/Calculadora.html', {'resultado': resultado})

        except Exception as e:
            return render(request, 'Proyectoweb/Calculadora.html', {'resultado': f'Error: {str(e)}'})
    
    return render(request, 'Proyectoweb/Calculadora.html')