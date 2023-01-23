secret_number = 777

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")
num = int(input('Ingresa tu número: '))
while num != secret_number:
    print('\n¡Ja, ja! ¡Estás atrapado en mi bucle!\n')
    num = int(input('Ingresa un nuevo número: '))

print('\n\n+====================================+')
print('¡Bien hecho, muggle! Eres libre ahora.')
print('+====================================+')
