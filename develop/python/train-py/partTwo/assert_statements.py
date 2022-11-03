#!/usr/bin/python3
# ========================= Assert Statements ==========================
# by Cosmosacm... tomado de Platzi
# 

# Divisores de un número
def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num%i == 0:
            divisors.append(i)
    return divisors        


def run():
    # lectura de datos del teclado
    num = input('\nIngresa un número: ')
    
    # condición para carácteres
    assert num.isnumeric(), '\nDebes ingresar un número'
    
    # condición números menores a 1
    assert int(num) > 0, '\nIngrese un número positivo'
    
    print('\nDivisores: \n' + str(divisors(int(num))))
    
    print('\n[!] Programa finalizado...')

if __name__ == '__main__':
    run()