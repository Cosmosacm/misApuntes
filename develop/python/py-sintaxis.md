# **Sintaxis Python**  

## **Caracteres Especiales**  

* **`\n`** : retorno de linea  
* **`\r`** : retorno de carro  
* **`\t`** : tabulador  
* **`\v`** : tabulador vertical  
* **`\\`** : backslash  
* **`\"`** : comilla doble  
* **`\'`** : comilla simple  
* **`\xNN`** : carácter hexadecimal NN en ascii  
* **`\uNN`** : carácter hexadecimal NN en unicode  
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

## **Funciones**  


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

