# ======================= Tablas de Multiplicar =======================
# by Cosmosacm...
# Calcula la tabla de multiplicar del numero que seleccione
#
def tabla(num: int):
    print('\nLa tabla de multiplicar del ' + str(num) + '\n')
    for i in range(1, 11):
        print(f'{num} X {i} = {num*i}')


def run():
    opcion = int(input('Elija un número al cual desea sacar su tabla'
                 + ' de multiplicar: '))
    tabla(opcion)


if __name__ == '__main__':
    run()