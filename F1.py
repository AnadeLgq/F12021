import csv
from datetime import datetime,timedelta

''' Calcula el total de puntos que obtuvo cada piloto al final de la temporada

    ENTRADA:
        - registros: lista de tuplas
    SALIDA:
        - puntos_totales: dicionario clave/valor de cada piloto (clave) y sus puntos totales (valor)
'''
def ranking_pilotos(registros):
    puntos_totales = {}
    for entrada in registros:
        if entrada[0] not in puntos_totales:
            puntos_totales[entrada[0]] = entrada[5]
        else:
            puntos_totales[entrada[0]] = puntos_totales[entrada[0]] + entrada[5]

    puntos_totales_ordenados = ordena_diccionario(puntos_totales)

    return puntos_totales_ordenados


'''Ordena un diccionario por sus valores
Fuente: https://stackabuse.com/how-to-sort-dictionary-by-value-in-python/

    ENTRADA:
        - dict_desordenado: diccionario desordenado
    SALIDA:
        - dict_ordenado: diccionario ordenado por valores
'''
def ordena_diccionario(dict_desordenado):
    valores_ordenados = sorted(dict_desordenado.values(), reverse=True) # Sort the values
    dict_ordenado = {}

    for i in valores_ordenados:
        for k in dict_desordenado.keys():
            if dict_desordenado[k] == i:
                dict_ordenado[k] = dict_desordenado[k]

    return dict_ordenado

# Imprimimos el mensaje de bienvenida y las opciones
print("Elige una opción por su número")
print("1. Ranking de pilotos por puntos")
print("2. Ranking de escuderias por puntos")
print("3. Vuelta mas rapida de cada circuito")

# Leemos la entrada del usuario
respuesta = input("Opción: ")

# Comprobamos la entrada del usuario
if respuesta in ["1", "2", "3"]:
    print("Has elegido la opción",respuesta)
else:
    print("Esa opción no se puede escoger, escoja de nuevo")

with open('F12021.csv', encoding='utf-8') as f:
    lector = csv.DictReader(f)
    registros = []
    for registro in lector:
        nombrePiloto = registro['nombrePiloto']
        referenciaPiloto = registro['referenciaPiloto']
        codigoPiloto = registro['codigoPiloto']
        posicion = int(registro['posicion'])
        # Para posteriormente poder comparar las vueltas rápidas de los pilotos, debemos procesarlas como timedeltas
        if registro['vueltaRapidaPersonal'] != '0':
             t = datetime.strptime(registro['vueltaRapidaPersonal'],'%M:%S.%f')
             vueltaRapidaPersonal = timedelta(minutes=t.minute, seconds=t.second, microseconds=t.microsecond)
        else:
            vueltaRapidaPersonal = timedelta(0)

        # En uno de los circuitos se dieron medios puntos, por eso usamos float
        puntos = float(registro['puntos'])
        nombreEscuderia = registro['nombreEscuderia']
        fecha = datetime.strptime(registro['fecha'], '%d/%m/%Y')
        nombreGP = registro['nombreGP']
        circuitoGP = registro['circuitoGP']
        ciudadGP = registro['ciudadGP']
        paisGP = registro['paisGP']

        tupla = (nombrePiloto, referenciaPiloto, codigoPiloto, posicion, vueltaRapidaPersonal, puntos, nombreEscuderia, fecha,nombreGP, circuitoGP, ciudadGP, paisGP)
        registros.append(tupla)

# En esta opción vamos a calcular todos los puntos de cada piloto y luego sacar una lista de mayor a menor según la puntuación. Esto último se mostrará por pantalla.
if respuesta == "1":
    ranking_pilotos(registros)
    print("El ranking de pilotos es:", ranking_pilotos(registros))
elif respuesta == "2":
    print("NO DISPONIBLE AÚN ;-;")
elif respuesta == "3":
    print("NO DISPONIBLE AÚN ;-;")
