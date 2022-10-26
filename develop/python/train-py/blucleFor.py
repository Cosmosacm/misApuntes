# ============================= Bucle For =============================
# by Cosmosacm... ejercicio tomado de @platzi
# * Realizar recorrido de un rango para imprimir elemento por elemento
# * Realizar recorrido de un string o cadena de texto carácter por 
#   carácter
#
def run():
    # función range con parámetro final, por defecto se inicia en cero.
    # definimos el blucle for
    for cont in range(5):
        print(cont)
    
    print(f'\nImprime los números del 0 al {cont} con incremento de 1')

    # separa sección
    separador = '--'
    print(separador.center(70, '-'))
    
    # función range con parámetro inicial y final
    # definimos el blucle for
    for cont in range(3, 10):
        print(cont)

    print(f'\nImprime los números del 3 al {cont} con incremento de 1')

    # separa sección
    separador = '--'
    print(separador.center(70, '-'))
    
    # función range con parámetro inicial, final y saltos
    # definimos el blucle for
    for cont in range(0, 20, 4):
        print(cont)

    print(f'\nImprime los números del 0 al {cont} con incremento de 4')

    # separa sección
    separador = '--'
    print(separador.center(70, '-'))

    # el rango a recorrer ahora es un elemento iterable como pueden ser
    # las cadenas de texto, las listas, las tuplas, etc...
    cadena = 'Cadena de texto impresa carácter por carácter'
    # definimos el blucle for
    for caracter in cadena:
        # con el end cambiamos el caracter al final de la impresión, que
        # por defecto es retorno de linea (\n)     
        print(caracter, end=', ')

    print(f'\nImprime los números del 0 al {cont} con incremento de 4')


if __name__ == '__main__':
    run()
