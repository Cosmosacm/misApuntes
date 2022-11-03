#!/usr/bin/python3
# ===================== Dictionary Comprehensions ======================
# by Cosmosacm... tomado de Platzi
# 

def run():
    # un dicicionario cuyas llaves son los 100 primeros números 
    # naturales y sus valores el cuadrado de su llave
    #
    # solución 1
    myDict1 = {}
    for i in range(1, 101):
        if i%3 != 0:
            myDict1[i] = i**3                                                                                                                                                                                                                                                                                   
    print(myDict1)
    #
    # separa sección
    separador = '--'
    print(separador.center(72, '-'))
    #
    # solución 2
    myDict2 = {i: i**3 for i in range(1,101) if i%3 != 0}
    print(myDict2)
    #
    # separa sección
    separador = '--'
    print(separador.center(72, '-'))
    # reto
    myDict3 = {i: round(i**0.5,2) for i in range(1, 1001)}
    print(myDict3)


if __name__ == '__main__':
    run()