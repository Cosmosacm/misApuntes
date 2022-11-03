#!/usr/bin/python3
# ============================ Diccionarios ============================
# by Cosmosacm... 
# Practicando con tuplas
#

def run():
    diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3
    }
    print(diccionario['llave1'])
    print(diccionario['llave3'])
    print(diccionario['llave2'])
    #
    poblacionPaises = {
        'Argentina': 78456578,
        'Brasil': 215457895,
        'Colombia': 54234612
    }
    print('\n')
    # lista de claves del diccionario
    print(poblacionPaises.keys())
    # recorrido de la lista para imprimer una a una cada clave
    for pais in poblacionPaises.keys():
        print(pais)
    print('\n')
    # lista de valores del diccionario
    print(poblacionPaises.values())
    # recorrido de la lista para imprimir uno a uno cada valor
    for poblaciones in poblacionPaises.values():
        print(poblaciones)
    print('\n')
    # lista donde cada elemento corresponde a una tupla que contiene una
    # clave y su valor respectivo iccionario
    print(poblacionPaises.items())
    # recorrido de la lista por elemento, imprime una tupla con clave y
    # valor en cada elemento
    for datos in poblacionPaises.items():
        print(datos)
    print('\n')
    for pais, poblacion in poblacionPaises.items():
        print(pais + ' tiene '+ str(poblacion) + 'habitantes')

if __name__ == '__main__':
    run()