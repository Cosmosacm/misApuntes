# **Funciones**  

Es un bloque de código que esta constituido por un conjunto de instrucciones para realizar una tarea en concreto.  

* La función debe estar definida con la palabra reservada `def`  
* Debe tener un nombre  
* Realizar una tarea especifica  
* Puede recibir parámetros para ser ejecutada  
* Puede devolver datos como resultado de ejecución  

## **Sintaxis de una función**  

* Sin parámetros

  ``` python
  def nombreFuncion():
      # bloque de código
      pass
  ```  

* Con parámetros

  ``` python
  def nombreFuncion(parametro1, parametro2,parametroN):
      # bloque de código
      pass
  ```  

  ``` python
    def nombreFuncion(parametro1: int, parametro2: str,parametroN: list):
        # bloque de código
        pass
    ```

## **Función principal para correr el programa**  

``` python
def run():
    # bloque de código
    pass
```  

## **Entry point o punto de entrada del programa**

``` python
if __name__ == '__main__':
    # ejecutar la función principal
    run()
```  

## **Métodos o Funciones buil-in**  

### **Métodos con string**  

Como ejemplo se toma variable como cualquier variable que contiene un string o una cadena de texto  

* `variable.strip()`: El método `strip` eliminará todos los espacios en blanco al inicio y al final de la cadena de caracteres de la variable.  
  * `lstrip()`: Eliminará los espacios en blanco al inicio.  
  * `rstrip()`: Eliminará los espacios en blanco al final.  

* `variable.lower()`: El método `lower` convertirá todas las letras en minúsculas.  
* `variable.upper()`: El método `upper` convertirá todas las letras en mayúsculas.  
* `variable.capitalize()`: El método `capitalize` convertirá la primera letra de la cadena de caracteres en mayúscula.  
* `variable.title()`: El método `title` convertirá la primera letra de cada palabra de una cadena en mayúscula.
* `variable.replace(‘caneda_a_buscar’, ‘cadena_nueva’)`: El método `replace` remplazará un cadena de texto por otra.  
* `len(variable)`: El método `len` calcula la longitud de la cadena de texto (total de caracteres) dentro de la variable.  
* `variable.count('cadena_a_buscar')`: El método `count` calcula la cantidad de veces que aparece una cadena de texto dentro de otra.  
* `variable.split('cadena_a_buscar')`: El método `split` convierte una cadena de texto en una lista de elementos separados por un caracter en concreto.  
* `variable.splitlines()`: El método `splitlines` convierte una cadena de texto en una lista de elementos que se encuentran separados por saltos de linea.  

* `variable.center(tamaño_total_cadena, 'carácter')`: El método `center` centra la cadena de texto de la variable dentro de una cadena de texto mayor de tamaño que desea utilizar, añadiendo el carácter deseado a la izquierda y a la derecha del mismo.  

### **Métodos con listas**  

list()  -> []  

* `lista.append(elemento)`: El método `append` agrega elementos al final de una lista.  
* `lista.pop(indice)`: El método `pop` elimina el elemento que se encuentra en la posición del indice dado, y lo retorna como respuesta. Si no se coloca indicide por defecto elimina el ultimo elemento.  
* `lista.sort()`: El método `sort` ordena la lista de menor a mayor.  
* `lista.sorted()`: El método `capitalize` convertirá la primera letra de la cadena de caracteres en mayúscula.
* del  
* remove  
* range  
* len  

### **Métodos con tuplas**  

tuple() -> ()

* `tupla.count(elemento)`: El método `count` busca el elemento dentro de la tupla y retorna la cantidad de coincidencias que encuentre.  
* `tupla.index(elemento, [star_index]..., [stop_index]..., )`: El método `index` busca el elemento dentro de la tupla y retorna index de la primera coincidencia que encuentre. Tiene como parametros opcionales el index desde donde quiero iniciar y el index hasta donde quiero parar.  

### **Métodos con diccionarios**  

dict() -> {}  

Es una estructura de datos mutable que almacena diferentes tipos de valores, sin importar su orden; identifican a cada elemento por una clave o llave (key), la cual tiene su respectivo  valor (value)

* `diccionario.keys()`: El método `keys` retornar las claves de un diccionario.  
* `diccionario.values()`: El método `values` retorna los valores de un diccionario.  
* `diccionario.items()`: El método `items` devuelve una lista de tuplas (primero la clave y luego el valor)

.clear() —> Elimina todos los items del diccionario

.pop(“n”) —> Elimina el elemento ingresado

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

---  

***[by Cosmosacm](https://cosmosacm.github.io/)***  
