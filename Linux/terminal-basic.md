
# **Terminal Basic**

#### **prompt:**  

    nombre_usuario@nombre_host:~$

#### **Comandos:**  

* un programa ejecutable como `xdg-open`, `code`, `libreoffice`
* un comando de utilidad de la shell como `cd`
* una función de shell
* un alias como `ls`

## **Sistema de archivos**  

### **Visualizar archivos:**  

`head`, `tail`, `less`, `cat`, `nano`, `more`, `vim`, `nvim`...  
`
### **Visualizar información:**  

`file`, `type`, `help`, `man`, `info`, `whatis`, `which`, `whoami`  

# **Abrir archivos/directorios:**  

Se utiliza el comando `xdg-open` para abrir programas y archivos desde la linea de comandos

* abrir editor de texto mousepad  
  `~$ xdg-open mousepad`  
* abrir visual studio code  
  `~$ xdg-open code`  
* abrir libre office  
  `~$ xdg-open libreoffice`  
* abrir archivo pdf  
  `~$ xdg-open name_file.pdf`  

### **Contatenar archivos:**  

Concatena las lineas del archivo file1 con las del archivo file2  

    ~$ cat file1 file2  

### **Crear archivos:**  

* crear un archivo con o sin extesión con el comando `touch` 

      ~$ touch name_file

* crear archivos con base a una entrada estándar proporcionada por el operador pipe, utilizando el comando `tee`  

      ~$ cat file1 file2 | tee union.txt      

### **Organizar archivos:**  

Organiza alfábeticamente o numericamente la información suministrada como una entrada estandar proporcionada por el comando pipe, utilizando el comando `sort`  

    ~$ cat file1 | sort  

## **Wildcards**  
| opción | acción |  
| :---: | :--- |
| **\*** | (asterisco) coincide con cualquier carácter |
| **\?** | (interrogación) conicide con cualquier carácter individual |
| **[caracteres]** | coincide con cualquier caracter que sea miembro del conjunto de carácteres |
| **[!caracteres]** | coincide con cualquier caracter que NO sea miembro del conjunto de carácteres |
| **[ [:clase:] ]** | coincide con cualquier caracter de la clase, ej de clases |

| tipos de clases | acción |  
| :---: | :--- |
| **[:alnum:]** | coincide con cualquier carácter alfanumérico |
| **[:alpha:]** | coincide con cualquier carácter alfábetico |
| **[:digit:]** | coincide con cualquier número |
| **[:upper:]** | coincide con cualquier letra mayúscula |
| **[:lower:]** | coincide con cualquier letra minúscula |

## **Entrada y Salida Estándar**  

Los datos en operaciones de entrada y salidad se organizan como archivo, es decir un flujo continuo de datos ordenados tal como lo es un archivo.  

### **Entrada estandar**  

**stdin 0** --> el teclado entrega un flujo de datos ordenado, lo que permite redireccionar los datos del teclado a un archivo.  

### **Salida estandar**  

**stdout 1**  -->   los comandos y programas también entregan un flujo de datos continuo que se ordena, por lo que se pueden redireccionar a un archivo.  

### **Error estandar**  

**stderr 2**  -->  

### **Redireccionamiento**  

| opción | acción |
| :---: | :--- |
| **\>** | redirecciona la salida estandar |
| **\>>** | concatena la salida con lo que este en el archivos|
| **2>** | redirecciona la salida error |
| **2>&1** | redirecciona la salida error y la salida estandar |

### **Operador pipe**  

Permite tomar la salida estandar de un comando y pasarla como entrada estandar a otro comando

### **Operadores de control**  

Permiten encadenar comandos:  

* **;** permite encadenar comandos en la misma linea, que se ejecutaran de manera sincrónica

* **&** permite encadenar comandos que se ejecutan de manera asincróna o de manera paralela, se ejecutan en segundo plano

* **&&**    permite encadenar comandos de manera condicional, si se cumple el primero se ejecuta el siguiente... condición **AND**

* **||**    permite encadenar comandos de manera codicional, si se cumple o no se cumple el primero  el siguiente siempre se ejecuta... condición **OR**  

## **Permisos**  

### Tipos de archivos  

1. **\-**    archivo
2. **d**    directorio  
3. **l**    enlace simbolico
4. **b**    bloque especial

## **Permisos de usuarios**  

1. propietario/owner  
2. grupo/group  
3. otros/world

### **Tipos de permisos**  

| opción | acción |  
| :---: | :--- |
| **r**  | lectura/readable |  
| **w**  | escritura/writeble |  
| **x**  | ejecución/executable |  

ej:  

```bash
name_user@name_host:~$ ls -lha
total 20K
drwxr-xr-x 3 name_user name_grupo 4.0K Sep 20 22:48 .
drwxr-xr-x 4 name_user name_grupo 4.0K Sep 20 11:29 ..
rw-r--r-- 1 name_user name_grupo 53 Sep 20 11:40 datos1
rw-r--r-- 1 name_user name_grupo 53 Sep 20 11:30 datos.txt
drwxr-xr-x 2 name_user name_grupo 4.0K Sep 20 22:48 prueba
```

| binario octal | propietario | grupo | otros |  
| :---: | :---: | :---: | :---: |
| 000   ->  0   | -           | -     | -     |
| 001   ->  1   | -           | -     | x     |
| 010   ->  2   | -           | w     | -     |
| 011   ->  3   | -           | w     | x     |
| 100   ->  4   | r           | -     | -     |
| 101   ->  5   | r           | -     | x     |
| 110   ->  6   | r           | w     | -     |
| 111   ->  7   | r           | w     | x     |

### **Modo simbolico**  

1. **u**    usuario  
2. **g**    grupo  
3. **o**    otros  
4. **a**    todos  

### **Modificar permisos**  

* **\+**   añade  
* **\-**   quita  
* **=**    asigna  

ej:  

```bash
~$ chmod 755 file                       rwxrw-rw-  

~$ chmod u+rwx,go+w file                rwxrw-rw-  

~$ chmod 644 file                       rw-r--r--  

~$ chmod u+rw-x,go+r-w+x file           rw-r--r--  

~$ chmod u=rwx,go=r file                rw-r--r--  
```

## **Cambiar de Usuario**  

```bash
~$ whoami                               visualiza usuario actual  
~$ su name_user                         cambia de usuario actual a name_user
~$ sudo su                              cambia de usuario actual a root  
```

## **Cambiar Password:**  

    ~$ passdw name_user

## **Enlace Simbolico**  

    ~$ ln -s /ruta/directorio/que/deseas/ nombre_link_simbolico  

## **Variables de Entorno**  

* imprimir todas las variables de entorno  

      ~$ printenv  

* imprimir el contenido de la variable de entorno  

      ~$ echo $VARIABLE_DE_ENTORNO  

Algunas variables de entorno:  

* indica el home del usuario 
  `~$ echo $HOME`  
* indica las rutas de donde estás los binarios que usa el sistema
  `~$ echo $PATH`  
* versión del bash utilizado  
  `~$ echo $BASH_VERSION`
* dirección de la shell que se esta utilizando  
  `~$ echo $SHELL`  

## **Comandos de Busqueda y Filtrado**  

```bash
~$ which nombre_comando                                  imprime la ruta de los binarios

~$ find ~/ruta/busqueda -name nombre_file                imprime de las coincidencias con nombre_file

~$ find ~/ruta/busqueda -name nombre_file | less

~$ find ~/ruta/busqueda -type d -name nombre_dir         d para directorios

~$ find ~/ruta/busqueda -type f -name *.log              f para archivo ej: .log

~$ find ~/ruta/busqueda -type l                          l para enlaces simbolicos

~$ find ~/ruta/busqueda -size 20M                        imprime archivos con tamaño igual a 20M

~$ find ~/ruta/busqueda -size +20M                       imprime archivos con tamaño mayor a 20M

~$ find ~/ruta/busqueda -size -20M                       imprime archivos con tamaño menor a 20M

~$ find ~/ruta/busqueda -type [d,f] -empty               imprime archivos/directorios vacios

~$ find ~/ruta/busqueda -type d -maxdepth 2              busca a máximo 2 directorios de profundidad

~$ find ~/ruta/busqueda -type d -mindepth 2              permite saltar niveles a minimo 2 directorios de profundidad
```

### **Comando grep** (Global Regular Expression Print)  

Realiza busquedas de texto dentro de un archivo, utilizando regex (Regular Expression) para realizar su búsqueda.

```bash
~$ grep [regex] [archivoDondeBuscar]

~$ grep -i [regex] [archivoDondeBuscar]                  i ignora el case sensitive

~$ grep -c [regex] [archivoDondeBuscar]                  c cuenta las ocurrencias

~$ grep -v [regex] [archivoDondeBuscar]                  v excluye la regex de la busqueda

~$ grep -m num_lineas [regex] [archivoDondeBuscar]       m limita las lineas de busqueda
```  

### **Comando cut**  

Extrae las partes seleccionadas de cada archivo en la salida estándar.  

* la opción d permite delimitar por el carácter a seleccionar entre las comillas, creando un determinado número de campos dependiendo de la coincidencia con el carácter.  

* la opción f seguido del número del campo, permite seleccionar el número del campo deseado  

ej: para seleccionar el texto 'es' se debe delimitar por espacio, creando 3 campos y filtral or el campo 3, seguido del pipe para delimitar por : y seleccionar el campo 1:  

    ~$ echo 'Mi nombre es:' | cut -d ' ' -f3 | cut -d ':' -f1  

### **Comando sed**  

Editor de texto en linea de comandos que permite extrar o filtrar texto de una entrada estandar por medio de expresiones regulares.  

la regex `'s/.$/char/` consta del campo s para sustituir, seguido el campo .$ que corresponde al ultimo valor de un texto, y el ultimo campo char corresponde al carácter a reemplazar.  

* se reemplaza el último valor por un =, cambiando los : por =  

      ~$ echo 'Mi nombre es:' | sed 's/.$/=/'  

* se reemplaza el último valor por nada, eliminando los :  

      ~$ echo 'Mi nombre es:' | sed 's/.$//'  

* se reemplaza los : por nada  

      ~$ echo 'Mi nombre es:' | sed 's/://'  

### **Comando tr**  

Traslada, comprime y/o elimina caracteres de la entrada estándar, escribiendo en la salida estándar.  

ej. elimina los : del texto  

    ~$ echo 'Mi nombre es:' | tr -d ':'

### **Comando awk**  

gawk es un lenguaje de reconocimiento y procesamiento de patrones. Por defecto lee la entrada estándar y escribe en la salida estándar.  

ej: reemplaza los : del texto por nada  

    ~$ echo 'Mi nombre es:' | awk 'sub(":","")'

### **Comando wc** (word count)  

Permite contar palabras, entrega cuatro elementos: 

* número_lineas  
* número_palabras  
* número_bits  
* nombre_file

      ~$ wc nombre_file          opciones: -l lineas, -w palabras, -c bytes, -m caracteres

## **Compresión y Descompresión**  

### **Comando tar**  

* Sintaxis utilizada para comprimir:  

  `~$ tar [opciones] [nombre_archivo_comprimido][archivo_a_comprimir/directorio_a_comprimir]`

      ~$ tar -cvf comprimido.tar misArchivos/            c compresión .tar
                                                        v verboso
                                                        f archivos
                 
      ~$ tar -czvf comprimido.tar.gz misArchivos/      z compresión .tar.gz o .tgz  

* Sintaxis utilizada para descomprimir:  

  `~$ tar [opciones] [nombre_archivo_comprimido]`  

      ~$ tar -xvf comprimido.tar       -x -> descompresión .tar

      ~$ tar -xzvf comprimir.tar.gz    -z -> descompresión .tar.gz o .tgz
  

### **Comando zip**  

* Sintaxis utilizada para comprimir:  

  `~$ zip [opciones] [nombre_archivo_comprimido] [archivo_a_comprimir/directorio_a_comprimir]`

      ~$ zip -r comprimido.zip misArchivos/        r recursivo

* Sintaxis utilizada para descomprimir:  

  `~$ unzip [opciones] [nombre_archivo_comprimido]`  

      ~$ unzip comprimido.zip  

## **Manejo de Procesos**  

### **Comando ps**  

muestra los procesos que se ejecutan en 4 columnas, PID, TTY, TIME, CMD  

      ~$ ps
  
* **PID** es el process ID
* **TTY** teletypewrite o teletipo, que es un dispositivo físco o virtual que permite interactuar con el sistema a nivel del kernel
* **TIME** medida de tiempo
* **CMD** nombre del proceso

### **Comando top**  

Muestra una interfaz con los procesos que se estan ejecutando más los recurso que consumen información adicional.  

    ~$ top  

### **Comando kill**

Mata el proceso seleccionado con el número de PID  

    ~$ kill numero_PID  

### **Comando htop**  

    ~$ htop

### **Comando glandes**  

    ~$ glandes
