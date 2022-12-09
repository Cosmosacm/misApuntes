# **Sintaxis Python**  

En Python si una variable se define con un único valor que no va a cambiar durante toda la ejecución del programa, se considera que es una constante.  

Python una variable definida en mayúscula la trata como una constante.  

    CONSTANTE = 3.141592

## **Caracteres Especiales**  

* **`\n`** : retorno de linea  
* **`\r`** : retorno de carro  
* **`\t`** : tabulador  
* **`\v`** : tabulador vertical  
* **`\\`** : backslash  
* **`\"`** : comillas doble  
* **`\'`** : comillas simple  
* **`\xNN`** : carácter hexadecimal NN en ASCII  
* **`\uNN`** : carácter hexadecimal NN en Unicode  
* **`\oNN`** : carácter octal NN  

## **Operadores Aritméticos**  

* **`+`** : sumar  
* **`-`** : restar, también se utiliza para asignar un valor negativo  
* **`*`** : multiplicar  
* **`/`** : dividir  
* **`//`** : división entera  
* **`%`** : módulo, obtiene el resto de la división  
* **`**`** : exponente  

### Orden de precedencia de los operadores aritméticos  

1. Operación exponente  
2. Operación negación  
3. Operaciones multiplicación, división, división entera y módulo  
4. Operaciones de suma y resta

## **Operadores Lógicos**  

Para trabajar con booleanos `verdadero = True`, `falso = False`  

* **`AND o &&`** : y  
* **`OR o ||`** : o  
* **`NOT o !`** : no  

## **Operadores de String**  

* **`+`** : concatena cadenas de texto.  

    ```python
    >>> 'Hola' + 'mundo'  
    Holamundo  
    ```  

* **`*`** : concatena n veces la misma cadena de texto.  

  ```python
  >>> 'Hola mundo'*3
  'Hola mundoHola mundoHola mundo'
  ```

* **`in`** : permite comprobar si un carácter o una cadena de texto está contenida dentro de otra cadena de texto.  

  ```python
  >>> 'nue' in 'Hola nuevo mundo'
  True
  >>> 'h' in 'Hola nuevo mundo'
  False
  >>> 
  ```

* **`[x:y]`** : permite extraer elementos consecutivos de una cadena de texto desde un punto inicial hasta un punto final.  

  ```python
  >>> 'hola mundo'[:3]
  'hol'
  >>> msg = 'hola mundo'
  >>> msg[2:8]
  'la mun'
  >>> msg[8:]
  'do'
  ```

## **Formateo del `print`**  

* **`sep`** permite modificar el carácter por defecto de espacio en blanco como separador.  

  ```python
  >>> print(1,21,3)
  1 21 3
  >>> print(1,21,3, sep=',')
  1,21,3
  ```

* **`end`** permite añadir una cadena de texto como elemento final del conjunto de elementos que se han enviado para mostrar, por defecto es un retorno de linea.  

  ```python
  >>> print(1,21,3)
  1 21 3
  # deja el cursor al lado del elemento final
  >>> print(1,21,3, end='.')
  1,21,3.>>>>
  # se añade elemento final y un retorno de linea
  >>> print(1,21,3, end='.\n')
  1,21,3.
  >>>>
  ```  

## **Formateo de Strings**  

### **Operador `%`**  

Indica que se va a sustituir un elemento en la cadena de texto, debe tener asociado un carácter que determina cual va a ser el tipo de dato que se desea sustituir; seguido de la cadena de texto se debe agregar la secuencia de los elementos que deseamos sustituir.  

* **`%c`** : un carácter  
* **`%s`** : cadena de texto  
* **`%d`** : número entero  
* **`%f`** : número real  
* **`%o`** : número octal  
* **`%x`** : número hexadecimal  

  ```python
  print('Yo tengo %d, tú tienes %d y ella tiene %d %s' % (30, 23, 26, 'años'))
  Yo tengo 30, tú tienes 23 y ella tiene 26 años
  ```

### **Función `format`**  

Esta conformada por los elementos que se desean agregar en una cadena de texto `.format(elem1, elem2, elem3,...)` y devuelve elementos formateados como string reemplazando cada elemento donde se encuentre el comodín conformado por la posición del elemento que deseamos reemplazar entre llaves `{elemX}`.  

```python
>>> print('Yo tengo {2} {3}, tú tienes {0} {3} y ella tiene {1} {3}'.format(23, 26, 30, 'años'))
Yo tengo 30 años, tú tienes 23 años y ella tiene 26 años
```

---  

***[by Cosmosacm](https://cosmosacm.github.io/)***  
