import math


def calcular_energia_cinetica(masa, velocidad):
    """
    Calcula la energía cinética de un objeto.

    Parámetros:
    masa (float) - la masa del objeto en kilogramos
    velocidad (float) - la velocidad del objeto en metros por segundo

    Retorna:
    float - la energía cinética del objeto en julios
    """
    return 0.5 * masa * velocidad**2

def calcular_energia_potencial(masa, altura, gravedad=9.8):
    """
    Calcula la energía potencial de un objeto.

    Parámetros:
    masa (float) - la masa del objeto en kilogramos
    altura (float) - la altura del objeto en metros
    gravedad (float) - la aceleración de la gravedad en metros por segundo cuadrado

    Retorna:
    float - la energía potencial del objeto en julios
    """
    return masa * gravedad * altura

def calcular_energia_mecanica(energia_cinetica, energia_potencial):
    """
    Calcula la energía mecánica de un objeto.

    Parámetros:
    energia_cinetica (float) - la energía cinética del objeto en julios
    energia_potencial (float) - la energía potencial del objeto en julios

    Retorna:
    float - la energía mecánica del objeto en julios
    """
    return energia_cinetica + energia_potencial

def calcular_trabajo(fuerza, distancia, angulo=0):
    """
    Calcula el trabajo realizado por una fuerza.

    Parámetros:
    fuerza (float) - la fuerza aplicada al objeto en newtons
    distancia (float) - la distancia que se mueve el objeto en metros
    angulo (float) - el ángulo entre la fuerza y la distancia en grados

    Retorna:
    float - el trabajo realizado en julios
    """
    return fuerza * distancia * math.cos(math.radians(angulo))

def calcular_caida_libre(altura):
    """
    Calcula el tiempo que tarda un objeto en caer desde una altura.

    Parámetros:
    altura (float) - la altura del objeto en metros

    Retorna:
    float - el tiempo que tarda el objeto en caer en segundos
    """
    return math.sqrt(2 * altura / 9.8)

def calcular_velocidad_final(velocidad_inicial, aceleracion, tiempo):
    """
    Calcula la velocidad final de un objeto.

    Parámetros:
    velocidad_inicial (float) - la velocidad inicial del objeto en metros por segundo
    aceleracion (float) - la aceleración del objeto en metros por segundo cuadrado
    tiempo (float) - el tiempo que tarda el objeto en moverse en segundos

    Retorna:
    float - la velocidad final del objeto en metros por segundo
    """
    return velocidad_inicial + aceleracion * tiempo

def calcular_altura_maxima(velocidad_inicial, aceleracion): 
    """
    Calcula la altura máxima de un objeto.

    Parámetros:
    velocidad_inicial (float) - la velocidad inicial del objeto en metros por segundo
    aceleracion (float) - la aceleración del objeto en metros por segundo cuadrado

    Retorna:
    float - la altura máxima del objeto en metros
    """
    return velocidad_inicial**2 / (2 * aceleracion)

def calcular_distancia_recorrida(velocidad_inicial, tiempo, aceleracion=0):
    """
    Calcula la distancia recorrida por un objeto.

    Parámetros:
    velocidad_inicial (float) - la velocidad inicial del objeto en metros por segundo
    tiempo (float) - el tiempo que tarda el objeto en moverse en segundos
    aceleracion (float) - la aceleración del objeto en metros por segundo cuadrado

    Retorna:
    float - la distancia recorrida por el objeto en metros
    """
    return velocidad_inicial * tiempo + 0.5 * aceleracion * tiempo**2

def calcular_fuerza(masa, aceleracion):
    """
    Calcula la fuerza de un objeto.

    Parámetros:
    masa (float) - la masa del objeto en kilogramos
    aceleracion (float) - la aceleración del objeto en metros por segundo cuadrado

    Retorna:
    float - la fuerza del objeto en newtons
    """
    return masa * aceleracion

def calcular_aceleracion(fuerza, masa):
    """
    Calcula la aceleración de un objeto.

    Parámetros:
    fuerza (float) - la fuerza aplicada al objeto en newtons
    masa (float) - la masa del objeto en kilogramos

    Retorna:
    float - la aceleración del objeto en metros por segundo cuadrado
    """
    return fuerza / masa

def calcular_masa(fuerza, aceleracion):
    """
    Calcula la masa de un objeto.

    Parámetros:
    fuerza (float) - la fuerza aplicada al objeto en newtons
    aceleracion (float) - la aceleración del objeto en metros por segundo cuadrado

    Retorna:
    float - la masa del objeto en kilogramos
    """
    return fuerza / aceleracion

def calcular_fuerza_elastica(constante_resorte, distancia):
    """
    Calcula la fuerza elástica de un resorte.

    Parámetros:
    constante_resorte (float) - la constante del resorte en newtons por metro
    distancia (float) - la distancia que se estira o comprime el resorte en metros

    Retorna:
    float - la fuerza elástica del resorte en newtons
    """
    return constante_resorte * distancia

def calcular_constante_resorte(fuerza_elastica, distancia):
    """
    Calcula la constante de un resorte.

    Parámetros:
    fuerza_elastica (float) - la fuerza elástica del resorte en newtons
    distancia (float) - la distancia que se estira o comprime el resorte en metros

    Retorna:
    float - la constante del resorte en newtons por metro
    """
    return fuerza_elastica / distancia