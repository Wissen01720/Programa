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
            if calculo in ['resistencia_serie', 'resistencia_paralelo']:
                resistencias = [float(request.POST.get(f'resistencia{i}')) for i in range(1, 3) if request.POST.get(f'resistencia{i}')]
                print(resistencias)  # Línea agregada
                if len(resistencias) < 2:
                    raise ValueError('Faltan valores de resistencia para el cálculo.')
                resultado = funciones_calculo[calculo](resistencias)
            elif calculo == 'resistencia_mixto':
                resistencias_serie = [float(request.POST.get(f'resistencia{i}')) for i in range(3, 5) if request.POST.get(f'resistencia{i}')]
                resistencias_paralelo = [float(request.POST.get('resistencia5'))] if request.POST.get('resistencia5') else []
                print(resistencias_serie, resistencias_paralelo)  # Línea agregada
                if len(resistencias_serie) < 2 or len(resistencias_paralelo) < 1:
                    raise ValueError('Faltan valores de resistencia para el cálculo.')
                resistencias = [resistencias_serie, resistencias_paralelo]
                resultado = funciones_calculo[calculo](resistencias)
            else:
                raise ValueError('Operación no reconocida')

            return render(request, 'Proyectoweb/Calculadora.html', {'resultado': resultado})
        except Exception as e:
            return render(request, 'Proyectoweb/Calculadora.html', {'resultado': f'Error: {str(e)}'})
    return render(request, 'Proyectoweb/Calculadora.html', {'resultado': 'No se ha enviado ningún formulario'})