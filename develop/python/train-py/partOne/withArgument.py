#!/usr/bin/python3
# ======================== Ingresar Argumentos =========================
# by Cosmosacm...
# * Como utilizar un programa ingresando argumentos
#

import sys

def suma(num1, num2):
    return num1 + num2


def run():
    if len(sys.argv) != 3:
        print('\n[!] No ingreso los agumentos correctos...')
        print('\nUso: python3 ' + sys.argv[0] + ' número_1 número_2')
        flat = False
        sys.exit(1)
    else:
        flat = True


    num1 = sys.argv[1]
    num2 = sys.argv[2]

    print('Tipo de datos leidos: ', type(num1), type(num2))

    result = suma(int(num1), int(num2))

    if flat:
        print('La suma de {0} más {1} es igual a {2}'.format(num1, num2, result))



if __name__ == '__main__':
    run()
