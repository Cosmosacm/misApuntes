# ========================== Break y Continue ==========================
# by Cosmosacm... ejercicio tomado de @platzi
# * continue permite saltar a una siguiente iteración en un bucle, y el
#   código debajo de el no se ejecuta.
# * break finaliza la ejecución de un bloque de código, como puede ser
#   un bucle, un condicional o una función.
#
from pyparsing import Char


def testContinue(miRango: int):
    # recorrido del rango
    for cont in range(miRango):
        # condicional y operación modulo 2 para tomar los números pares
        if cont%2 != 0:
            # ingresa si es impar y no se ejecuta el print
            continue
        # imprimir cada número par separado por un espacio
        print(cont, end=' ')


def testBreak(texto: str, letra: Char):
    # recorrido de un string
    for cont in texto:
        # condicional entre el cáracter y la letra elegida
        if cont == letra:
            # si el cáracter es igual a la letra elegida termina for
            break
        print(cont, end=' ')    

def run():
    # ingresar un número
    num = int(input('\nDigite un número: '))
    print(f'\nEstos son todos los numeros pares hasta el {num}: \n')
    # ejecutar función
    testContinue(num)

    # separa sección
    print(' ')
    separador = '--'

    # ingresar un texto
    frase = input('\nIngrese una frase : ')
    letra = input('\nIngrese cualquier letra que este contenida en la '
                  + 'frase: ')
    print('\nSe imprimen todos los carácteres de la frase hasta '
          + f'encontrar la primera letra "{letra}"\n')
    testBreak(frase, letra)

if __name__ == '__main__':
    run()
