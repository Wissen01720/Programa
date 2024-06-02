import math


def calcular_resistencias_circuitoSerie(resistencias):
    """
    Calcula la resistencia total de un circuito en serie.

    Parámetros:
    resistencias (list) - una lista de resistencias en ohms

    Retorna:
    float - la resistencia total del circuito en ohms
    """
    resistencia_total = 0
    for resistencia in resistencias:
        resistencia_total += resistencia
    return resistencia_total

def calcular_resistencias_circuitoParalelo(resistencias):
    """
    Calcula la resistencia total de un circuito en paralelo.

    Parámetros:
    resistencias (list) - una lista de resistencias en ohms

    Retorna:
    float - la resistencia total del circuito en ohms
    """
    resistencia_total = 0
    for resistencia in resistencias:
        resistencia_total += 1 / resistencia
    return 1 / resistencia_total

def calcular_resistencia_circuitoMixto(resistencias):
    """
    Calcula la resistencia total de un circuito mixto.

    Parámetros:
    resistencias (list) - una lista de resistencias en ohms

    Retorna:
    float - la resistencia total del circuito en ohms
    """
    resistencia_total = 0
    resistencias_serie = []
    resistencias_paralelo = []
    for resistencia in resistencias:
        if isinstance(resistencia, list):
            resistencias_paralelo.append(calcular_resistencias_circuitoParalelo(resistencia))
        else:
            resistencias_serie.append(resistencia)
    resistencia_total = calcular_resistencias_circuitoSerie(resistencias_serie)
    resistencia_total += calcular_resistencias_circuitoParalelo(resistencias_paralelo)
    return resistencia_total