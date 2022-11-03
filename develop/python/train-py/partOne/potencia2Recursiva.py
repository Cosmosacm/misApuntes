# =========================== Potencia de 2 ===========================
# tomado de Juan Esteban Galvis en @platzi
# Calcula la potencia de dos hasta un numero de potencias deseada
# realizandolo de una manera recursiva si utilizar bucles
#
def run(num, rept):
    if num <= rept:
        # cont = num
        print(str(2**num))
        run(num+1, rept)
    else:
        print("Fin!")

if __name__ == "__main__":
    repeticiones = int(input("Cuantas potencias: "))
    run(0, repeticiones)