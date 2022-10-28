#!/usr/bin/python3
# ========================== Es Número Primo ==========================
# by Cosmosacm...
# Validar si un número es primo, que solo sea divisible por si mismo y 
# la unidad
#
from curses.ascii import isdigit
from pyrsistent import v

from sympy import div


# imprime una linea de guiones para separar secciones
def resaltarTxt(texto: str, numero_lineas: int, longitud: int, 
                caracterH: str, caracterV: str):
    # valida si la longitud máxima para el string es par o impar
    if longitud%2 == 0:
        h = 2*caracterH
        # se anexan 2 espacios
        v = '  '
        # valida si el tamaño del texto es par o impar
        if (len(texto)%2) == 0:
            texto = ' ' + texto + ' '
        else:
            texto = ' ' + texto + '  '
    else:
        h = caracterH
        # se anexa 1 espacio
        v = ' '
        # valida si el tamaño del texto es par o impar
        if len(texto)%2 == 0:
            texto = ' ' + texto + '  '
        else:
            texto = ' ' + texto + ' '
    # construción del marco y el contenido
    for i in range(2*numero_lineas + 3):
        # se inserta el carácter a lado y lado del texto
        if i == 0:
            print(h.center(longitud, caracterH))
        elif i == 2*numero_lineas + 2:
            print(h.center(longitud, caracterH))
        elif i == numero_lineas + 1:
            # se insertan espacios a lado y lado del texto y dos pipes
            print(texto.center(longitud - 2, ' ').center(longitud, caracterV))
        else:
            print(v.center(longitud - 2, ' ').center(longitud, caracterV))



# imprime una linea de guiones para separar secciones
def separador(numero_secciones: int):
    # separa sección
    for i in range(numero_secciones):
        separador = '--'
        print(separador.center(72, '-'))


# limpia el prompt de la terminal
def cleanDisplay():
    pass


# imprime un mensaje inicial
def msgInicio():
    # mensaje inicial
    msg = ' ¿Es Número Primo? '
    # adición de caracteres al mensaje inicial para destacarlo
    msg = msg.center(71, '=')
    # impresión mensaje inicial
    msg = f'''\n{msg}\n\nValida si un número es primo!
        '''
    print(msg)


# imprime el mensaje del menú de opciones
def msgMenu():
    # separa sección
    separador(1)
    # mensajes del menú
    print('\n\tMenú Principal\n')
    print('\nEligue una de las siguientes opciones:\n')
    print('1. Validar si un número es primo')
    print('2. Validar los números primos de una lista (separar con '
          + 'comas o espacios)')
    print('3. Para salir digite: "s" o "salir" o "q" o "quit"\n')
    # separa sección
    separador(1)


# permite confirmar la salida del programa
def salir():
    # mensaje saliendo
    msgSalir = '[!] Saliendo...'
    # variable boolena a retornar
    salida = True
    # variable bloolena para controlar el bucle while
    val = True
    # bucle while para validar la opción ingresada
    while val:
        # confirmar salir del programa
        confirmar = input('\n\nSeguro desea salir del programa [S/N]: ')
        # se eliminan espacios y se convierte todo a minúscula
        confirmar = confirmar.lower().strip()
        #
        if confirmar == 'salir':
            break
        elif confirmar == 's':
            break
        elif confirmar == 'quit':
            break
        elif confirmar == 'q':
            break
        elif confirmar == 'n':
            salida = False
            msgSalir = ''
            val = False
        elif confirmar == 'no':
            salida = False
            msgSalir = ''
            val = False
        else:
            cleanDisplay()
            print('\nLa opción ingresada no es valida\n')
    return [salida, msgSalir]


# menú principal para elegir las opciones a ejecutar
def menu():
    # mensaje menú
    msgMenu()
    # variable bloolena para controlar el bucle while
    val = True
    # bucle while para validar la opción ingresada
    while val:
        # opción ingresada por el usuario
        opcion = input('\nIngrese el número de la opción: ')
        # se eliminan espacios y se convierte todo a minúscula
        opcion = opcion.lower().strip()
        if opcion == '1':
            break
        elif opcion == '2':
            break
        elif opcion == '3':
            break
        elif opcion == 'salir':
            opcion = '3'
            break
        elif opcion == 's':
            opcion = '3'
            break
        elif opcion == 'quit':
            opcion = '3'
            break
        elif opcion == 'q':
            opcion = '3'
            break
        else:
            print('\nLa opción ingresada no es valida\n')
            # mensaje menú
            msgMenu()
    # variable que retorna la opción seleccionada
    return int(opcion)
        

""" def ctrl_l():
    print('Fin del programa... presionaste "ctrl+l"')
    return False  """ 


def continuar():
    # variable bloolena para controlar el bucle while
    val = True
    # bucle while para validar la opción ingresada
    while val:
        # continuar con un nuevo número o salir
        confirmar = input('\n Desea validar un nuevo número [S/N]: ')
        # se eliminan espacios y se convierte todo a minúscula
        confirmar = confirmar.lower().strip()
        #
        if confirmar == ('n' or 'no' or 'q' or 'salir' or 'quit'):
            new = False
            val = False
        elif confirmar == 's':
            # variable boolena a retornar
            new = True
            val = False
        else:
            cleanDisplay()
            print('\nLa opción ingresada no es valida\n')
    return new


def numPrimo(numero: int):
    # mensajes
    msgPrimo = f'El número {numero} es primo!'
    msgNoprimo = f'El número {numero} No es primo!'
    # condicional para validar los divisores del número
    if numero%2 == 0:
        # el número es par, tiene al menos un divisor
        if numero == 2:
            # es primo
            divisor = False
        else:
            # existe un divisor
            divisor = True
    else:
        # se validan los números impares
        # hasta la mitad del número a calcular
        mitad = numero//2
        # el rango inicia en 3, hasta la mitad más 1 en saltos de 2 en 2
        if numero == 1 or numero == 3 or numero == 5:
            # es primo
            divisor = False
        else:
            for i in range(3, (mitad + 1), 2):
                if numero%i == 0:
                    # existe un divisor
                    divisor = True
                    break
                else:
                    # no es divisor
                    divisor = False
    # validar si existe un divisor
    if divisor:
        # tiene divisor no es primo
        return msgNoprimo
    else:
        # no tiene divisor es primo
        return msgPrimo

def opcion1():
    # variable bloolena para controlar el bucle while
    val = True
    while val:
        # ingreso del número a validar
        numStr = input('\n\nDigita el número que deseas validar: ')
        # valida si es número o string
        if numStr.isdigit() == False:
            # no es un número, es un string
            numStr = numStr.lower()
            if numStr == 'salir':
                break
            elif numStr == 's':
                break
            elif numStr == 'quit':
                break
            elif numStr == 'q':
                break
            else:
                cleanDisplay()
                print('\nHubo un error, por favor ingrese un número '
                      + 'valido\n')
        else:
            # es un número
            # valor del número máximo permitido
            LIMITE = 1000000
            num = int(numStr)
            if num > LIMITE:
                cleanDisplay()
                # mensaje de error
                print('\nHubo un error, por favor ingrese un número '
                      + f'menor a {LIMITE}\n')
            else:
                # mensaje de validación es o no primo
                msg = numPrimo(num)
                # se realta el mensaje
                print('\n\n')
                resaltarTxt(msg, 3, 72, '#', '#')
                # if continuar():
                #     continue
                # else:    
                #     # salir de opción 1
                #     val = False


def run():
    # mensaje inicial
    msgInicio()
    # variable bloolena para controlar el bucle while
    val = True
    while val:
        # menú de opciones
        opcion = menu()
        if opcion == 1:
            opcion1()
        elif opcion == 2:
            pass
        elif opcion == 3:
            # seleccionó salir
            salida = salir()
            # autoriza salir
            if salida[0]:
                print('\n\n')
                print(salida[1])
                # terminar bucle while
                val = False
            

if __name__ == '__main__':
    run()