# ============================ Bucle While ============================
# by Cosmosacm... tomado de @platzi
# Calcula la potencia de dos hasta llegar ha un limite definido
#
def run():
    # python una variable definida en mayúscula la trata como una constante
    # limite para calcular las potencias de 2
    LIMITE = 1000000
    # variable contador
    cont = 0
    potencia2 = 2**cont
    # definimos el blucle while
    while potencia2 < LIMITE:
        print('2 elevado a ' + str(cont) + ' es igual a: '
              + str(potencia2))
        cont += 1
        potencia2 = 2**cont


if __name__ == '__main__':
    run()
