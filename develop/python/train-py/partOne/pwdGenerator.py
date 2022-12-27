#!/usr/bin/python3
# ========================= Password Generator =========================
# Copyright by Cosmosacm...
# * Genera contraseñas de manera aleatoria de manera segura
# * se puede elegir el tamaño de caracteres de la contraseña
# * puede contener: números, letras mayúsculas y minúsculas, caracteres 
#   especiales 
# 

import random
import string


def pwdGenerator(size: int):
    # tupla con números de tipo string
    num = tuple('0123456789')
    # tupla con letras de la a-z concatenado con de la A-Z.
    letters = tuple(string.ascii_letters)
    # tupla con caracteres especiales
    specialCharts = tuple(string.punctuation)
    # concatenar tuplas
    allCharts = letters + num + specialCharts + num
    # variable de tipo lista
    password = []
    for i in range(size):
        selectChart = random.choice(allCharts)
        password.append(selectChart)
    
    return ''.join(password)

def run():
    # variable booleana para controlar el bucle while
    val = True
    # bucle while para validar la opción ingresada
    while val:
        # ingresar tamaño contraseña
        size = input('\nIngrese el tamaño de la contraseña: ')
        size = size.lower().strip()
        # validar tamaño contraseña
        if size.isdigit():
            if int(size) < 14:
                print('\n[!] El tamaño mínimo es de 14 caracteres\n')
                # separa sección
                separador = '--'
                print(separador.center(72, '-'))
            elif int(size) >256:
                print('\n[!] El tamaño máximo es de 256 caracteres\n')
                # separa sección
                separador = '--'
                print(separador.center(72, '-'))
            else:
                break
        else:
            print('\n[!] Error, debe seleccionar solo números\n')
            # separa sección
            separador = '--'
            print(separador.center(72, '-'))
    #
    pwdNew = pwdGenerator(int(size))
    print('\n\n')
    # separa sección
    separador = ''
    print(separador.center(72, '='))
    print('Tu nueva contraseña es: \n\n' + pwdNew)
    # separa sección
    separador = ''
    print(separador.center(72, '='))

if __name__ == '__main__':
    run()