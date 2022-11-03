#!/usr/bin/python3
# ======================== List Comprehensions ========================
# by Cosmosacm... tomado de Platzi
#  


def square1():
    # solución 1
    square = []
    for i in range (1,101):
        # validar si el número no es divisible entre 3
        if i%3 != 0:
            square.append(i**2)
    print(square)


def square2():
    # solución 2 list comprehensions
    square2 = [i**2 for i in range(1,101) if i%3 != 0]
    print(square2)


def multiples469():
    # solución 1 
    # con condicionales
    multiples1 = [i for i in range(1, 100000) if i%4 == 0 and
                  i%6 == 0 and i%9 == 0]
    print(multiples1)

    # solución 2
    # se calcula el máximo común divisor de 4, 6 y 9 = 36
    multiples2 = [i for i in range(1, 100000) if i%36 == 0]
    print(multiples2)


def run():
    # 100 primeros números naturales al cuadrado no divisibles por 3
    # solución 1
    square1()
    
    # separa sección
    separador = '--'
    print(separador.center(72, '-'))
    
    # solución 2
    square2()

    # separa sección
    separador = '--'
    print(separador.center(72, '-'))
    
    # Todos lol múltiplos de 4, 6, 9  hasta 5 dígitos
    multiples469()




if __name__ == '__main__':
    run()