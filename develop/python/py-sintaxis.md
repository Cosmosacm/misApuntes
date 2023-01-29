# **Sintaxis Python**  

## **Variables**  

Una variable es un espacio en memoria en el que se puede almacenar el valor de cualquier tipo de dato en Python.  

Las variables tienen 3 componentes:

* Constan de un nombre con el cual se identifica.  
* Deben tener un valor o valores del dato que se almacena.  
* Tienen un tipo de dato.  

### **Operador de Asignación**  

El igual **`=`** es un operador de asignación utilizado para asignar un valor de un determinado tipo de dato a una variable.  

```python
var1 = 5
var2 = 'Mi nombre'
x = y
```

### **Constantes**  

En Python si una variable se define con un único valor que no va a cambiar durante toda la ejecución del programa, se considera que es una constante.

Python una variable definida en mayúscula la trata como una constante.  

```python
CONSTANTE = 3.141592
```

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

### **Orden de precedencia de los operadores aritméticos**  

1. Operación exponente  
2. Operación negación  
3. Operaciones multiplicación, división, división entera y módulo  
4. Operaciones de suma y resta

## **Operadores de Comparación o Relacionales**  

Se utilizan para comparar valores, retornan como resultado valores booleanos `verdadero = True`, `falso = False`  

* **Igual a: `==`**  

  ```python
  >>> 5 == 5
  True
  >>> 5 == 3
  False
  ```

* **No es igual a: `!=`**  
* **Mayor qué: `>`**  
* **Mayor o igual qué: `>=`**  
* **Menor qué: `<`**  
* **Menor o igual qué: `<=`**  

## **Operadores Lógicos**  

Se utilizan para realizar operaciones booleanas, trabajan con booleanos `verdadero = True`, `falso = False`  

* **`and`** : y  
* **`or`** : o  
* **`not`** : no  

## **Operadores Bit a Bit**  

Permiten manipular bits de datos individuales y realizan las operaciones lógicas bit a bit.

**Nota**: solo funcionan con números enteros.

* **`&`** : and
* **`|`** : or  
* **`~`** : not  
* **`~`** : xor (o exclusivo)  

### **Shifting**  

Desplazamiento binario a la izquierda y desplazamiento binario a la derecha.  

* El shifting a la izquierda consiste en agregar un cero a nivel de bits a la derecha del número lo que equivale a multiplicar por dos.
  
  ```python
  >>> 7 << 1
  14  # equivalente a decir 7 = 111 al desplazar un bit a la izquierda tenemos 1110 = 14
  
  >>> 2 << 2
  8   # equivalente a decir 2 = 10 al desplazar dos bit a la izquierda tenemos 1000 = 8
  ```

* El shifting a la derecha consiste en quitar el primer bit a la derecha del número lo que equivale a dividir por dos.

  ```python
  >>> 5 >> 1
  2  # equivalente a decir 5 = 101 al desplazar un bit a la derecha tenemos 10 = 2
  
  >>> 7 >> 2
  1   # equivalente a decir 7 = 111 al desplazar dos bit a la derecha tenemos 1 = 1
  ```

## **Orden de Precedencia de Operadores**  

| Prioridad | Operador | Observación |
| :--: | :--: | :-- |
| 1 | `~`, `+`, `-` | negación bit a bit, signo positivo, signo negativo |
| 2 | `**`  | Exponente |
| 3 | `*`, `/`, `//`, `%` | multiplicación, división, división entera y módulo |
| 4 | `+`, `-` | Suma y resta |
| 5 | `<<`, `>>` | Shifting |
| 6 | `>`, `>=`, `<`, `<=`  | Mayor, mayor o igual, menor, menor o igual |
| 7 | `==, !=`  | Igualdad, desigualdad |  
| 8 | `&` | and bit a bit |  
| 9 | `\|` | or bit a bit |  
| 10 | `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `&=`, `\|=`, `<<=`, `>>=` | Operaciones |  

## **Operadores in y not in**  

Son capaces de revisar una lista para verificar si un valor específico está almacenado dentro de la lista o no.  

### **in**  

Verifica si un elemento dado está actualmente almacenado en algún lugar dentro de una lista o un iterable a validar, el operador devuelve `True` si existe o `False` si no existe.  

```python
elemento in lista_a_validar

>>> 'o' in 'Python'
True  

>>> 'a' in 'Python'
False  
```  

### **not in**

Verifica si un elemento dado está ausente en una lista o un iterable, el operador devuelve `True` si no existe o `False` si existe.  

```python
elemento not in lista_a_validar

>>> 10 not in [1, 2, 3, 4, 5, 6, 7, 8]
True

>>> 3 not in [1, 2, 3, 4, 5, 6, 7, 8]
False
```  


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
  >>> 'hola mundo'[:3]+
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

Ejemplo:

```python
>>> print('Yo tengo %d, tú tienes %d y ella tiene %d %s' % (30, 23, 26, 'años'))
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
