# **Funciones y Métodos**  

## **Funciones**  

Es un bloque de código que esta constituido por un conjunto de instrucciones para realizar una tarea en concreto.  

* La función debe estar definida con la palabra reservada `def`.  
* Debe tener un nombre.  
* Realizar una tarea especifica.  
* Puede recibir parámetros para ser ejecutada.  
* Puede devolver datos como resultado de ejecución.  

### **De donde provienen las funciones**  

* Hay funciones que son parte integral del lenguaje de programación y siempre están disponibles, se llaman **funciones integrales**.

  ```python
  print()
  input()
  int()
  float()
  len()
  ```

* Hay funciones que provienen de módulos pre-instalados en el lenguaje de programación, para ser utilizadas se debe primero importar el módulo al que pertenece la función a utilizar.  
  
  ```python
  import math
  math.sqrt()   # Raíz cuadrada
  math.sin()    # Función seno
  
  import time
  time.sleep()  # Retrasa la ejecución durante un número determinado de segundos
  ```

* Hay funciones propias o definidas por el usuario que se pueden crear directamente en el código.  

  ```python
  def saludo():
    print('Hola mundo')
  
  saludo()
  ```

* Existen funciones que se relacionan con clases.  

## **Sintaxis de una función**  

### **Sin parámetros**  

  ```python
  # Definición de la función
  def nombreFuncion():
      # bloque de código
  
  # Invocación de la función
  nombreFuncion()
  ```  

### **Con parámetros**  

Especificar uno o más parámetros en la definición de la función es un requerimiento, y se debe de cumplir durante la invocación de la misma. Se debe proveer el mismo número de argumentos como haya parámetros definidos.

* Paso de parámetros posicionales, asigna cada argumento al parámetro correspondiente de acuerdo a su posición:

  ``` python
  # Definición de la función
  def nombreFuncion(parametro1, parametro2, parametroN):
      # bloque de código
  
  # Invocación de la función
  nombreFuncion(argumento1, argumento2, argumentoN)     
  ```  

* Paso de argumentos de palabra clave, donde el significado del argumento está definido por su nombre, no su posición:  

  ``` python
  # Definición de la función
  def nombreFuncion(parametro1, parametro2, parametroN):
      # bloque de código
  
  # Invocación de la función
  nombreFuncion(parametro1 = argumento1, parametro2 = argumento2, parametroN = argumentoN)     
  ```  

* Especificación de parámetros de acuerdo a su tipo de dato:  

  ```python
  # Definición de la función
  def nombreFuncion(parametro1: int, parametro2: str, parametroN: list):
      # bloque de código
    
  # Invocación de la función
  nombreFuncion(23, 'Saludos', [1, 2])     
  ```

* Funciones parametrizadas, para predefinir valores a los argumentos los cuales pueden ser considerados cuando los argumentos correspondientes han sido omitidos:  

  ```python
  # Definición de la función
  def nombreFuncion(gravedad=9.8 , planeta='Tierra' , lunas=None):
      # bloque de código
  
  # Invocación de la función
  nombreFuncion(3.72, 'Marte', 2)           # g = 3.72 planeta= 'marte' lunas= 2
  nombreFuncion(lunas=1)                    # g = 9.8 planeta= 'tierra' lunas= 1
  nombreFuncion(planeta='planetaX23')       # g = 9.8 planeta= 'planetaX23' lunas= None
  ```

### **Función principal para correr el programa**  

```python
def run():
    # bloque de código
```

### **Entry point o punto de entrada del programa**

```python
if __name__ == '__main__':
    # ejecutar la función principal
    run()
```  

## **Instrucción return**  

La instrucción `return` se utiliza para que las funciones devuelvan, regresen o retornen un valor.  

* **`return`** sin expresión, se utiliza para terminar la función, y se asume que devuelve implícitamente como valor llamado `None`.

  ```python
  def nombreFuncion():
      # bloque de código
      return
  ```  

* **`return`** con expresión, termina la función y transporta el valor de la expresión al lugar donde se ha invocado función.  

  ```python
  def nombreFuncion():
      # bloque de código
      return expression
  
  resultado = nombreFuncion()     # retorna el valor de la expresión de la función en la variable resultado
  ```  

### **Valor None**  

El valor **`None`** en realidad no es un valor en lo absoluto, por lo tanto, no debe participar en ninguna operación, porque causa una excepción de tipo TypeError.  

Solo existen dos tipos de circunstancias en las que `None` se puede usar de manera segura:  

* Cuando se le asigna a una variable (o se devuelve como el resultado de una función).

* Cuando se compara con una variable para diagnosticar su estado interno.

## **Métodos**  

Un método es un tipo específico de función - se comporta como una función y se parece a una función, pero difiere en la forma en que actúa y en su estilo de invocación.  

Un método es propiedad de los datos para los que trabaja, mientras que una función es propiedad de todo el código.  

## **Sintaxis de una Método**  

* Sin parámetros

  ```python
  resultado = datos.metodo()

  >>> texto = 'Aprende a programar'
  >>> texto.upper()
  'APRENDE A PROGRAMAR'
  ```  

* Con parámetros

  ``` python
  resultado = datos.metodo(parametro1, parametro2, parametroN)
  
  >>> texto = 'Aprende a programar'
  >>> texto.center(72, '=')
  '==========================Aprende a programar==========================='
  ```  

## **Métodos o Funciones build-in**  

### **Métodos con string**  

Como ejemplo se toma variable como una variable que contiene un string o cadena de texto.  

* **Método para concatenar**  

  Este es mejor manera de realizar una concatenación

  | Command | Definition |
  | :-- | :-- |
  | `variable1.join(variable2)` | El método `join` permite concatenar string o cadenas de texto que provengan de una variable iterable (variable2), también permite insertar un determinado string (variable1) entre cada elemento de la variable iterable. |

  ```python
    >>> '-*-'.join(['Aprendiendo', 'python'])
    'Aprendiendo-*-python'

    >>> '='.join('hola')
    'h=o=l=a'

    >>> ' '.join(['Hola', 'mundo', 'con','Python',str(3)])
    'Hola mundo con Python 3'
    ```  

* **Métodos que devuelven un nuevo string**  

  | Command | Definition |
  | :-- | :-- |
  | `variable.strip()` | El método `strip` eliminará todos los espacios en blanco al inicio y al final |
  | `variable.lstrip()` | Eliminará los espacios en blanco al inicio |
  | `variable.rstrip()` | Eliminará los espacios en blanco al final |  
  | `variable.lower()` | El método `lower` convertirá todas las letras en minúsculas |
  | `variable.upper()` | El método `upper` convertirá todas las letras en mayúsculas |
  | `variable.capitalize()` | El método `capitalize` convertirá la primera letra en mayúscula |
  | `variable.title()` | El método `title` convertirá la primera letra de cada palabra en mayúscula |
  | `variable.swapcase()` | El método `swapcase` invierte las mayúsculas por minúsculas y viceversa |
  | `variable.replace(‘cadena_a_buscar’, ‘cadena_nueva’)` | El método `replace` remplazará una cadena de texto por otra |
  | `len(variable)` | El método `len` calcula la longitud de la cadena de texto (total de caracteres del string) |
  | `max(variable)` | El método `max` identifica en el string el carácter alfabético mayor |
  | `min(variable)` | El método `min` identifica en el string el carácter alfabético menor |
  | `variable.count('cadena_a_buscar')` | El método `count` calcula la cantidad de veces que aparece una cadena de texto dentro de otra |
  | `variable.split('cadena_a_buscar')` | El método `split` convierte una cadena de texto en una lista de elementos separados por un carácter en concreto |
  | `variable.splitlines()` | El método `splitlines` convierte una cadena de texto en una lista de elementos que se encuentran separados por saltos de linea |
  | `variable.find('cadena_a_buscar')` | El método `find` busca una cadena de texto dentro de la variable de izquierda a derecha |
  | `variable.rfind('cadena_a_buscar')` | El método `rfind` busca una cadena de texto dentro de la variable de derecha a izquierda |
  | `variable.center(tamaño_total_cadena, 'carácter')` | El método `center` centra el contenido de la variable dentro de una cadena de texto de mayor tamaño, añadiendo el carácter deseado a la izquierda y a la derecha de la variable |
  | `variable.ljust(tamaño_total_cadena, 'carácter')` | El método `ljust` ajusta a la izquierda el contenido de la variable dentro de una cadena de texto de mayor tamaño, añadiendo el carácter deseado a la derecha de la variable |
  | `variable.rjust(tamaño_total_cadena, 'carácter')` | El método `rjust` ajusta a la derecha el contenido de la variable dentro de una cadena de texto de mayor tamaño, añadiendo el carácter deseado a la izquierda de la variable |
  | `variable.zfill(tamaño_total_cadena)` | El método `zfill` ajusta a la derecha el contenido de la variable dentro de una cadena de texto de mayor tamaño, añadiendo ceros (0) a la izquierda de la variable |

* **Métodos que devuelven un True o False**  
  Nota: los signos de puntuación ni los espacios en blanco son caracteres alfabéticos  

  | Command | Definition |
  | :-- | :-- |
  | `variable.isalnum()` | El método `isalnum` comprueba si todos los caracteres que componen el string son alfanuméricos (letras y números) o no |
  | `variable.isalpha()` | El método `isalpha` comprueba si todos los caracteres que componen el string son alfabéticos (solo letras) o no |
  | `variable.isdigit()` | El método `isdigit` comprueba si todos los caracteres que componen el string son dígitos o no |
  | `variable.isnumeric()` | El método `isnumeric` comprueba si todos los caracteres que componen el string tienen un representación numérica o no |
  | `variable.isdecimalt()` | El método `isdecimal` comprueba si todos los caracteres que componen el string tienen una representación numérica decimal o no |
  | `variable.islower()` | El método `islower` comprueba si todos los caracteres que componen el string están en minúscula o no |
  | `variable.isupper()` | El método `isupper` comprueba si todos los caracteres que componen el string están en mayúscula o no |
  | `variable.istitle()` | El método `istitle` comprueba si el primer carácter de todas las palabras que componen el string están en mayúscula y el resto de caracteres en minúscula o no |
  | `variable.isprintable()` | El método `isprintable` comprueba si todos los caracteres que componen el string son imprimibles  o no |
  | `variable.isspacer()` | El método `isspacer` comprueba si todos los caracteres que componen el string son caracteres en blaco o no |
  | `variable.startwith('cadena_a_buscar')` | El método `starwith` comprueba si una cadena de texto a buscar esta contenida al inicio en el string o no |
  | `variable.endtwith('cadena_a_buscar')` | El método `endwith` comprueba si una cadena de texto a buscar esta contenida al final en el string o no |

### **Métodos con listas**  

list()  -> []  

| Command | Definition |
| :-- | :-- |
| `lista.append(elemento)` | El método `append` agrega elementos al final de una lista |
| `lista.pop(indice)` | El método `pop` elimina el elemento que se encuentra en la posición del indice dado, y lo retorna como respuesta. Si no se coloca índice por defecto elimina el ultimo elemento |
| `lista.sort()`| El método `sort` ordena la lista de menor a mayor |
| `lista.sorted()` | El método `sorted` convertirá la primera letra de la cadena de caracteres en mayúscula |
| `del lista[indice]` | La instrucción `del` elimina el elemento del indice seleccionado y disminuye el tamaño de la lista |
| `lista.remove(elemento)` | El método `remove` elimina la primera coincidencia del valor del elemento que se encuentre en la lista. Si no hay coincidencia se genera la excepción ValueError |  
| `range(start, stop, step)` | `range` es un función que devuelve una secuencia de enteros desde start hasta stop (excluyente) con incrementos de step |
| len | pendiente |

### **Métodos con tuplas**  

tuple() -> ()

| Command | Definition |
| :-- | :-- |
| `tupla.count(elemento)` | El método `count` busca el elemento dentro de la tupla y retorna la cantidad de coincidencias que encuentre |
| `tupla.index(elemento, [star_index]..., [stop_index]..., )` | El método `index` busca el elemento dentro de la tupla y retorna index de la primera coincidencia que encuentre. Tiene como parámetros opcionales el index desde donde quiero iniciar y el index hasta donde quiero parar |

### **Métodos con diccionarios**  

dict() -> {}  

Es una estructura de datos mutable que almacena diferentes tipos de valores, sin importar su orden; identifican a cada elemento por una clave o llave (key), la cual tiene su respectivo  valor (value)

| Command | Definition |
| :-- | :-- |
| `diccionario.keys()` | El método `keys` retornar las claves de un diccionario |
| `diccionario.values()` | El método `values` retorna los valores de un diccionario |
| `diccionario.items()` | El método `items` devuelve una lista de tuplas (primero la clave y luego el valor) |
| `diccionario.clear()` | Elimina todos los items del diccionario |
| `diccionario.pop(“n”)` | Elimina el elemento ingresado |

## **Funciones Anónimas**

Es una función que no tiene un identificador (**sin nombre**), y que tienen una serie de características particulares; en python se le conocen como **lambda function**.  

La funciones lambda pueden tener los **argumentos** que se necesiten, pero solo **una línea de código**.  

**El resultado** de una función lambda **se almacena** en una **variable**, la cual se va a utilizar como el identificar de una función lambda en particular.  

Sintaxis: **`lambda argumentos: expresión`**  

## **High Order Functions**  

Es una función que recibe como parámetro otra función.  

Ej:

```python
# función de orden superior
def saludo(func):
    func()

#función 1
def hola():
    print('Hola buen día!!!')

# función 2
def adios():
    print('Adios!!!')

# 
saludo(hola)
saludo(adios)

# resultado
Hola buen día!!!
Adios!!!
```  

### **Filter**  

```python
myList = [1, 8, 5, 15, 42, 23, 54]

# extraer impares con list comprehension
odd1 = [i for i in myList if i%2 != 0] 
print(odd1)

# extraer impares con filter
odd2 = lis(filter(lambda i: i%2 != 0, myList))
print(odd2)
```  

### **Map**  

```python
myList = [1, 2, 3, 4, 5]

# convertir los números de la lista a sus cuadrados
square1 = [i**2 for i in myList]

# convertir los números de la lista a sus cuadrados
square2 = list(map(lambda i: i**2, myList))
```  

### **Reduce**  

```python
myList = [2, 2, 2, 2, 2]

# multiplicar elemento por elemento
allMultiplied1 = 1

for i in myList:
    allMultiplied1 *= i

print(allMultiplied1)

#
from functools import reduce

allMultiplied2 = reduce(lambda x, y: x*y, myList)

print(allMultiplied2)
```  

## **Generadores**

* Son estructuras que extraen valores de una función y se almacenan en objetos iterables (que se pueden recorrer).  

* Los valores se almacenan de uno en uno.  

* Cuando un generador almacena un valor, queda en un estado pausado, hasta que se solicite el siguiente valor, característica que se conoce como **suspensión de estado**.  

---  

***[by Cosmosacm](https://cosmosacm.github.io/)***  
