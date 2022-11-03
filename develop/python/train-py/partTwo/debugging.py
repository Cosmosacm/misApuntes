#!/usr/bin/python3
# ============================== Debuggin ==============================
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
    try:
        num = int(input('\nIngresa un número: '))
        try:
            if num <= 0:
                raise TypeError('\nIngrese un número positivo')
            print('\nDivisores: \n'+ str(divisors(num)))
        except TypeError as err:
                print(err)       
    except ValueError:
        print('\nDebes ingresar un número')
    finally:
        print('\n[!] Programa finalizado...')

if __name__ == '__main__':
    run()