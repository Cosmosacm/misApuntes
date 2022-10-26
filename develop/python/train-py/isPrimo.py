# ========================== Es Número Primo ==========================
# by Cosmosacm...
# Validar si un número es divisible solo por si mismo y la unidad, es
# decir es un número primo
#
from curses.ascii import isdigit

def msgMenu():
    msg = ' ¿Es Número Primo? '
    msg = msg.center(71, '=')
    msg = f'''\n{msg}\n\nValida si un número es primo!
        '''
    print(msg)
    print('\nPara salir del programa digite la letra "s"\n')


# def ctrl_l():
#     print('Fin del programa... presionaste "ctrl+l"')
#     return False    


def run():
    # funcion mensaje de entrada
    msgMenu()
    val = True
    while val:
        num = input('Digita el número que deseas validar: ')
        if num.isdigit() == False:
            if num.lower() == 's':
                print('Fin del programa')
                break
            else:
                print('\nHubo un error, por favor ingrese un número '
                      + 'valido\n')
                continue
        else:
            LIMITE = 1000000
            if int(num) > LIMITE:
                print('\nHubo un error, por favor ingrese un número '
                    + f'menor a {LIMITE} \n')
                continue
        val = False


if __name__ == '__main__':
    run()