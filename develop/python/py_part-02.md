# **Python Part Two**  

## **Documentation**  

### **Zen of python**  

El Zen de python son los **20 principios de software** más importantes que tiene el lenguaje de python, que fue elaborado por Tim Peters.  

Para visualizar el **zen de python**, en la consola interactiva de python se ingresa el comando `import this`.  

### **PEP (Python Enhancement Proposals)**  

Se refiere a las **propuestas de mejora de python**, y contiene la documentación que conforma las **guías de estilos** del lenguaje, el **como funciona** y **como se debería escribir** de manera correcta.

## **Entorno de Desarrollo Linux**  

Instalar Python 3 y librerías necesarias.  

```bash
~$ sudo apt update

~$ sudo apt upgrade -y

~$ sudo apt install python3 -y

~$ sudo apt install python3-pip -y

~$ sudo apt install build-essential libssl-dev libffi-dev python3-dev -y
```

## **Modules**

Un modulo es un código escrito por nosotros mismos u otras personas creado para solucionar un problema en particular o proporcionar funcionalidades. El código se puede reutilizar de manera rápida en otros programas para evitar estar reinventando la rueda en cada ocasión.  

## **Virtual Environment**  

Un **entorno virtual** en python es un **espacio de trabajo separado** en el que el interprete de python, las librerías o bibliotecas, y los scripts instalados en él, están **aislados** del sistema principal de python y de otros entornos virtuales; como si fuese un contenedor con un python a la medida de las necesidades a requerir.  

* **Como crear un entorno virtual**  
`python3 -m venv name_entorno`
  * **`python3`** es el comando de python utilizado en Linux, Mac y Windows  
  * **`-m`** es un flat o bandera que indica que se utilizará un módulo interno del lenguaje  
  * **`venv`** corresponde al módulo de entornos virtuales (virtual environment)  
  * **`name_entorno`** es el nombre que le daremos al entorno virtual para identificarlo, por convención se utiliza venv  

```bash
# crear entorno virtual
~$ python3 -m venv name_entorno

~$ ls
name_entorno

# contenido del entorno virtual
~$ ls name_entorno
bin  include  lib  lib64  pyvenv.cfg

# contenido directorio bin ... en Windows el directorio bin se llama Scripts
~$ ls name_entorno/bin/
activate  activate.csh  activate.fish  Activate.ps1  pip  pip3  pip3.10  python  python3  python3.10
```  

* **Como acceder al entorno virtual**  
  * Linux y Mac: **`source name_entorno/bin/activate`**  
    crear un alias en .bashrc: `alias nombre-alias="comando"`  
    ej: `alias avenv='venv/bin/activate'`
  * Windows: **`.\name_entorno\Scripts\activate`**
    crear un alias: `alias nombre-alias="comando"`  
    ej: `alias avenv='.\name_entorno\Scripts\activate'`

```bash
# acceder al entorno virtual... 
# el nombre del entorno virtual aparece al inicio del prompt
~$ source name_entorno/bin/activate
(name_entorno) ~$ 

# salir del entorno virtual...
# desaparece el nombre del entorno virtual al inicio del prompt
(name_entorno) ~$ deactivate
~$  
```  

## **Package Installer**  

### **Manejadores de paquetes**  

* **`pip`** (viene por defecto en python)
* **`pyenv`**  

### **Módulos populares**  

* Requests  
* BeutifulSoup4  
* Pandas  
* Numpy  
* Pytest  

* **Validar versión pip**  

```bash
# valida la versión de pip y muestra la versión de python utilizada
(name_entorno) ~$ pip3 -V
pip 22.3 from tu_ruta/name_entorno/lib/python3.10/site-packages/pip (python 3.10)
```  

* **Validar módulos instalados**  

`pip3 freeze`  

```bash
# muestra los módulos instalados hasta el momento
(name_entorno) ~$ pip3 freeze
(name_entorno) ~$
```  

* **Instalar módulos**  

`pip3 install nombre_modulo`  

```bash
(name_entorno) ~$ pip3 install pandas
(name_entorno) ~$ pip3 freeze
numpy==1.23.4
pandas==1.5.1
python-dateutil==2.8.2
pytz==2022.5
six==1.16.0
```  

* **Compartir dependencias**  

  `pip3 freeze > requirements.txt`

```bash
# archivos y directorios del entorno virtual
(name_entorno) ~$ ls
name_entorno

# creación archivo requirements con la información de los módulos del entorno virtual
(name_entorno) ~$ pip3 freeze > requirements.txt
(name_entorno) ~$ ls
requirements.txt  venv01

# contenido del archivo requirements.txt
(name_entorno) ~$ cat requirements.txt
numpy==1.23.4
pandas==1.5.1
python-dateutil==2.8.2
pytz==2022.5
six==1.16.0

# clona las dependencias de un entorno virtual para replicarlo
(name_entorno) ~$ pip3 install -r requirements.txt
```  

## **List Comprehensions**  

`[element for element in iterable if condition]`

* `element` representa a cada uno de los elementos a poner en la nueva lista  
* `for element in iterable` ciclo a partir del cual se extraerán elementos de otra lista o cualquier iterable  
* `if condition`condición opcional para filtrar los elementos del ciclo  

```python
# 100 primeros números naturales al cuadrado no divisibles por 3
listSquare = [i**2 for i in range(1, 101) if i%3 !=0]
```  

## **Dictionary Comprehensions**  

`[key: value for value in iterable if condition]`

* `key` representa a cada uno de las llaves a poner en el nuevo diccionario  
* `value` representa a cada uno de los valores a poner en el nuevo diccionario  
* `for value in iterable` ciclo a partir del cual se extraerán elementos de otra lista o cualquier iterable  
* `if condition`condición opcional para filtrar los elementos del ciclo  

```python
# llave y valor de los 100 primeros números naturales al cubo no divisibles por 3
myDict = [i: i**3 for i in range(1, 101) if i%3 !=0]
```  

## **Errores**  

### **SyntaxError**  

En en los errores de sintaxis python detiene el programa y no ejecuta ni si quiera la primera linea de código.  

### **Exception**  

Las excepciones ocurren en alguna parte del programa y hacen que este quiebre el resto de la lógica.  

Python muestra los errores de excepciones a través del mensaje denominado **traceback**, y este mensaje se lee de abajo hacia arriba o desde el final hacia el inicio.  

1. La última línea muestra el **tipo de excepción** y una **breve explicación** del error.
2. La penúltima línea muestra el nombre del archivo (**File**), en caso de estar en la consola interactiva aparece **"\<stdin\>"**.  
3. La antepenultima línea muestra la traza del error, explicando de donde parte el error.

Ejemplo de algunas excepciones:

* **`KeyboardInterrupt`**: ocurre cuando pulsamos `ctrl+C` en la consola interactiva de python, se corta el proceso y todo se cierra; python eleva la excepción desde dentro hacia afuera y termina el proceso.  
* **`KeyError`**: ocurre cuando intentamos acceder a una llave que no existe en un diccionario.  
* **`IndexError`**: ocurre cuando intentamos acceder a un indice que no existe una lista.  
* **`FileNotFoundError`**: ocurre cuando intentamos abrir un archivo que no existe.  
* **`ZeroDivisionError`**: ocurre cuando intentamos dividir un número entre cero.  
* **`ImportError`**: ocurre cuando intentamos importar un módulo, y existe algún error en el módulo y este falla.

## **Debugging**  

Es la acción de hacer depuración de un código para encontrar errores en las funcionalidades del programa que el lenguaje de programación no detecta. Para hacerlo de manera eficiente se utiliza una herramienta para hacer depuración con vscode.  

## **Manejo de Excepciones**  

### **try, except**

Probar y excepto que, hacer lo siguiente.

```python
try: 
    bloque_código_A   # sección try

except Tipo_Error:
    bloque_código_B   # sección except

bloque_código_C
```  

1. La sección **`try`** prueba todo el bloque de código de dicha sección `código_bloque_A`.  
Si no se presentan excepciones, el flujo del programa sigue un curso normal y no se ejecuta la sección `except` y pasa al siguiente bloque de código `bloque_código_C`.
2. Si ocurre una excepción en el bloque de código de la sección del `try` entonces, el flujo del programa pasa a la sección del `except`, aquí se captura la excepción.  
    * Si la excepción capturada corresponde al mismo tipo de error definido `Tipo_Error`, entonces se ejecuta el bloque de código `bloque_código_B` de la sección `except`.  
    * Si la excepción capturada no corresponde al mismo tipo de error definido `Tipo_Error`. entonces la excepción se levanta y cierra el programa mostrando el mensaje **traceback**.  

Ej:

```python
def unaFunc(var: str):
    print('Ingresaste este texto: ' + var)

try:
    unaFunc(7)
except TypeError:
    print('[!] Solo puede ingresar texto')
```  

### **rise**

```python

```  

Ej:

```python
def palindrome(texto):
    try:
        if len(texto) == 0:
          raise ValueError('No se puede ingresar una cadena vacía')
        return texto == texto[::-1]
    except ValueError as err
        print(err)
        return False


try:
    print(palindrome(''))
except TypeError:
    print('[!] Solo puede ingresar texto')
```  

### **finally**

Se utiliza al final de una estructura `try, except` para realizar una de las siguientes opciones:

* Cerrar un archivo dentro de python  
* Cerrar una conexión a una base de datos  
* Liberar recursos externos  

```python
try:
    f = open('archivo.txt')
    # hacer cualquier cosa con el archivo
    bloque_código
finally:
    # ejecuta este código exista un error o no 
    f.close()
```  

Ej:

```python
def palindrome(texto):
    try:
        if len(texto) == 0:
          raise ValueError('No se puede ingresar una cadena vácia')
        return texto == texto[::-1]
    except ValueError as err
        print(err)
        return False


try:
    print(palindrome(''))
except TypeError:
    print('[!] Solo puede ingresar texto')
```  

## **Assert Statements**  

Afirmo que esta condición es verdadera, sino corte el programa e imprima este mensaje de error

Sintaxis: **`assert condición, mensaje de error`**

```python
def palindrome(texto):
    msgErr = 'No se puede ingresar una cadena vacía'
    assert len(texto) > 0, msgErr
    return texto == texto[::-1]


print(palindrome(''))
```  

## **Archivos**  

* **Archivo de texto:** tienen bytes que solo representan caracteres como letras, números, símbolos, etc.  

  `.txt`, `.json`, `.xml`, `.py`, `.js`, `.csv`, `.css`

* **Archivos binarios:** tienen bytes que representan infinitamente cosas más complejas.

  `.png`, `.jpg`, `.mp3`, `.dll`, `.avi`, `.mp4`

### **Modos de apertura**  

* **R** lectura  
* **W** escritura (sobrescribir)  
* **A** escritura (agregar al final)  

r -> Solo lectura
r+ -> Lectura y escritura
w -> Solo escritura. Sobre escribe el archivo si existe. Crea el archivo si no existe
w+ -> Escritura y lectura. Sobre escribe el archivo si existe. Crea el archivo si no existe
a -> Añadido (agregar contenido). Crea el archivo si éste no existe
a+ -> Añadido (agregar contenido) y lectura. Crea el archivo si éste no existe.

Con respecto a lo mencionado por allí desde el minuto 1:46 hasta 2:33 aprox… realmente puedes manejar archivos .mp3, .mp4, .jpg, .png en python…es el pan nuestro de cada día en el area de visión artificial en donde librerías como openCV lo hacen bastante amigable e interesante…
por ejemplo, un video en formato .mp4 es perfectamente transformable en una matriz numérica que representa por medio de estos número los canales RGB que posee cada pixel y que en general almacena la totalidad del pixeles de una imagen…

dejo este enlace para quien tenga curiosidad:

https://docs.opencv.org/master/d7/da8/tutorial_table_of_content_imgproc.html  

Para trabajar con archivos de M. Excel se puede utilizar el módulo OpenPyXL :

Lectura y escritura de libros
Creación y acceso a las hojas de cálculo
Creación de fórmulas de Excel
Creación de gráficos, con apoyo de otros módulos
OpenPyXL no hace parte de las librerias estándar de Python y por ello se requiere instalar:

Modos de apertura

‘r’: Por defecto, para leer el fichero.
‘w’: Para escribir en el fichero.
‘x’: Para la creación, fallando si ya existe.
‘a’: Para añadir contenido a un fichero existente.
‘b’: Para abrir en modo binario.
'r’+ Lectura y escritura
'w+ Escritura y lectura. Sobre escribe el archivo si existe. Crea el archivo si no existe
'a+’ Añadido (agregar contenido) y lectura. Crea el archivo si éste no existe.

```python
with open('./ruta/del/archivo.txt', 'r', encoding='utf-0') as nombre_identificador:
```  

Reto final:

Hangman Game: el juego del ahorcado.

Reglas:

* Incorporar comprehensions, manejo de errores, y manejo de archivos  
* Utiliza el archivo data.txt y leelo para obtener las palbras

Ayudas y pistas:

* Investiga la función enumerate  
* método get de los diccionarios puede servirte  
* La sentencia para limpiar la pantalla  
    os.system('cls') -> windows
    os.system('clear') -> unix

Mejora el juego  

* añade un sistema de puntos  
* dibuja el ahorcado en cada jugada con código ascii
* mejora la interfaz

https://github.com/santigo171/python-hangman

@facmartoni 
facundonicolas.com
---  

***[by Cosmosacm](https://cosmosacm.github.io/)***  