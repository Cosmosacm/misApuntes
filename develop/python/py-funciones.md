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
