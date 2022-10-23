# ============================= Palindrómo =============================
# Aquella palabra o frase que se puede leer igual de izquierda a derecha
# como de derecha a izquierda

# Función para determinar si una palabra o una frase es palíndromo
def palindromo(txt: str):
    # eliminamos los espacios
    txt = txt.replace(' ', '')
    # convertimos toda la cadena en minúscula
    txt = txt.lower()
    # creamos una nueva variable con el texto invertido
    invtxt = txt[::-1]
    # comparamos si la palabra o frase es igual al derecho que al revés
    if txt == invtxt:
        return True
    else:
        return False


# Función principal para correr el programa
def run():
    texto = input('\nEscribe una palabra o una frase: ')
    isPalindromo = palindromo(texto)
    if isPalindromo == True:
        print('Es palíndromo')
    else:
        print('No es palíndromo')


# Entry point o punto de entrada del programa
if __name__ == '__main__':
    # ejecuta la función principal
    run()



