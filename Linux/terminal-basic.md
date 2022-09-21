
# **Terminal Basic**

#### **prompt:**  

        nombre_usuario@nombre_host:~$

#### **Comandos:**  

* un programa ejecutable como `xdg-open`, `code`, `libreoffice`
* un comando de utilidad de la shell como `cd`
* una función de shell
* un alias com `ls`

## **Sistema de archivos**  

**visualizar archivos:**    `head`, `tail`, `less`, `cat`, `nano`, `more`...  

**visualizar información:** `file`, `type`, `help`, `man`, `info`, `whatis`, `which`, `whoami`  

**abrir archivos/directorios:**  

* `$ xdg-open mousepad`   --> abre el editor de texto mousepad  
* `$ xdg-open code`   --> abre visual studio code
* `$ xdg-open libreoffice`   --> abre el libre office  

**contatenar archivos:**  

* `~$ cat file1 file2`  --> concatena las lineas del archivo file1 con las del archivo file2  

**crear archivos:**

* `~$ touch nombreArchivo`  

* `~$ tee`   --> crea archivos con base a una entrada  

        ~$ cat file1 file2 | tee union.txt  

**organizar archivos:**  

* `sort` --> organiza alfábeticamente o numericamente la información suministrada con base en una salida  

        ~$ cat file1 | sort  

## **Wildcards**  

* **\***    --> (asterisco) coincide con cualquier carácter  
* **\?**    --> (interrogación) conicide con cualquier carácter individual  
* **[caracteres]**    --> coincide con cualquier caracter que sea miembro del conjunto de carácteres  
* **[!caracteres]**  --> coincide con cualquier caracter que NO sea miembro del conjunto de carácteres
* **[ [:clase:] ]**   --> coincide con cualquier caracter de la clase, ej de clases  

    1. **[:alnum:]**    coincide con cualquier carácter alfanumérico  
    2. **[:alpha:]**    coincide con cualquier carácter alfábetico  
    3. **[:digit:]**    coincide con cualquier número
    4. **[:upper:]**    coincide con cualquier letra mayúscula
    5. **[:lower:]**    coincide con cualquier letra minúscula

## **Entrada y Salida Estandar**  

Los datos en operaciones de entrada y salidad se organizan como archivo, es decir un flujo continuo de datos ordenados tal como lo es un archivo.  

### **Entrada estandar**  

**stdin 0** --> el teclado entrega un flujo de datos ordenado, lo que permite redireccionar los datos del teclado a un archivo.  

### **Salida estandar**  

**stdout 1**  -->   los comandos y programas también entregan un flujo de datos continuo que se ordena, por lo que se pueden redireccionar a un archivo.  

### **Error estandar**  

**stderr 2**  -->  

### **Redireccionamiento**

* **\>**    redirecciona la salida estandar  
* **\>>**   concatena la salida con lo que este en el archivos  
* **2>**    redirecciona la salida error  
* **2>&1**  redirecciona la salida error y la salida estandar  
        
        
#### **Operador pipe**  

Permite tomar la salida estandar de un comando y pasarla como entrada estandar a otro comando

#### **Operadores de control**  

Permiten encadenar comandos:  

* **;** permite encadenar comandos en la misma linea que se ejecutaran de manera sincrónica

* **&** permite encadenar comandos que se ejecutan de manera asincróna o de manera paralela, se ejecutan en segundo plano

* **&&**    permite encadenar comandos de manera condicional, si se cumple el primero se ejecuta el siguiente... condición **AND**

* **||**    permite encadenar comandos de manera codicional, si se cumple o no se cumple el primero  el siguiente siempre se ejecuta... condición **OR**  

## **Permisos**  

### Tipos de archivos  

1. **\-**    archivo
2. **d**    directorio  
3. **l**    enlace simbolico
4. **b**    bloque especial

### Permisos de usuarios  

1. propietario/owner  
2. grupo/group  
3. otros/world

### Tipos de permisos  

1. **r**    lectura/readable  
2. **w**    escritura/writeble  
3. **x**    ejecución/executable

| binario octal | propietario | grupo | otros |  
| ------------- | ----------- | ----- | ----- |
| 000   ->  0   | -           | -     | -     |
| 001   ->  1   | -           | -     | x     |
| 010   ->  2   | -           | w     | -     |
| 011   ->  3   | -           | w     | x     |
| 100   ->  4   | r           | -     | -     |
| 101   ->  5   | r           | -     | x     |
| 110   ->  6   | r           | w     | -     |
| 111   ->  7   | r           | w     | x     |

### Modo simbolico  

1. **u**    usuario  
2. **g**    grupo  
3. **o**    otros  
4. **a**    todos  

### Modificar permisos  

1. **\+**   añade  
2. **\-**   quita  
3. **=**    asigna  

        ~$ chmod 755 file                rwxrw-rw-  

        ~$ chmod u+rwx,go+w file         rwxrw-rw-  

        ~$ chmod 644 file                rw-r--r--  

        ~$ chmod u+rw-x,go+r-w+x file    rw-r--r--  

        ~$ chmod u=rwx,go=r file         rw-r--r--  

### Cambiar de usuario  

        ~$ whoami                    --> usuario actual  
        ~$ su nombre_usuario         --> usuario actual a usuario a switchar
        ~$ sudo su                   --> usuario actual a usuario root  
                        
### Cambiar password:  
        ~$ passdw nombre_usuario
    

### Enlace simbolico  

        ~$ ln -s /ruta/directorio/que/deseas/ nombre_link_simbolico
    
### **Variables de entorno**  

                            $ printenv                      --> imprime todas las variables de entorno

                            $ echo $VARIABLE_DE_ENTORNO     --> imprime el contenido de la variable de entorno

                            HOME            -->     indica el home del usuario 
                            PATH            -->     indica las rutas de donde estás los binarios que usa el sistema
                            BASH_VERSION    -->     versión del bash utilizado
                            SHELL           -->     dirección de la shell que se esta utilizando

    Comandos de busqueda:
                        
                $ which nombre_comando                                  --> imprime la ruta de los binarios

                $ find ~/ruta/busqueda -name nombre_file            --> imprime de las coincidencias con nombre_file
                $ find ~/ruta/busqueda -name nombre_file | less     --> aplica el comando less para visualizar mejor el archivo
                $ find ~/ruta/busqueda -type d -name nombre_dir     --> tipo d para directorios
                $ find ~/ruta/busqueda -type f -name *.log          --> tipo f para archivo ej: extensión .log
                $ find ~/ruta/busqueda -type l                      --> tipo l para enlaces simbolicos
                $ find ~/ruta/busqueda -size 20M                    --> imprime los archivos con tamaño igual a 20M
                $ find ~/ruta/busqueda -size +20M                   --> imprime los archivos con tamaño mayor a 20M
                $ find ~/ruta/busqueda -size -20M                   --> imprime los archivos con tamaño menor a 20M
                $ find ~/ruta/busqueda -type [d,f] -empty           --> imprime los archivos/directorios vacios                                                                                                                                                                                                                                                                                                                                                                                                     
                $ find ~/ruta/busqueda -type d -maxdepth 2          --> limita la busqueda a máximo 2 directorios de profundidad
                $ find ~/ruta/busqueda -type d -mindepth 2          --> permite saltar niveles a minimo 2 directorios de 
                                                                        profundidad

    
    Comando grep
                    realiza busquedas de texto dentro dentro de un archivo, utilizando regex (Regular Expression) para realizar 
                    su búsqueda. Grep” significa Global Regular Expression Print. 

                $ grep [ExpresiónRegular] [archivoDondeBuscar]
                $ grep -i [ExpresiónRegular] [archivoDondeBuscar]                   --> -i ignora el case sensitive
                $ grep -c [ExpresiónRegular] [archivoDondeBuscar]                   --> -c cuenta las ocurrencias
                $ grep -v [ExpresiónRegular] [archivoDondeBuscar]                   --> -v excluye la expresión regular de la busqueda
                $ grep -m numero_lineas [ExpresiónRegular] [archivoDondeBuscar]     --> -m limita las lineas de busqueda
                    
    Comando word count

                permite contar palabras

                $ wc nombre_file        --> entrega cuatro elementos    
                                            numero_lineas, número_palabras, número_bits, nombre_file
                                                    
                                            opciones:   -l lineas, -w palabras, -c bytes, -m caracteres

    Compresión:
                $ tar [opciones] [nombre_archivo_comprimido][archivo_a_comprimir/directorio_a_comprimir]

                $ tar -cvf comprimido.tar misArchivos/          -c -> compresión .tar
                                                                -v -> verboso
                                                                -f -> archivos
                                
                $ tar -czvf comprimido.tar.gz misArchivos/      -z -> compresión .tar.gz o .tgz

                $ zip [opciones] [nombre_archivo_comprimido] [archivo_a_comprimir/directorio_a_comprimir]

                $ zip -r comprimido.zip misArchivos/

    
    Descompresión:

                $ tar [opciones] [nombre_archivo_comprimido]
                
                $ tar -xvf comprimido.tar       -x -> descompresión .tar

                $ tar -xzvf comprimir.tar.gz    -z -> descompresión .tar.gz o .tgz
                
                $ unzip [opciones] [nombre_archivo_comprimido]

                $ unzip comprimido.zip

    
    Manejo de procesos:

                $ ps                    --> muestra los procesos que se ejecutan en 4 columnas, PID, TTY, TIME, CMD
                                        --> PID es el process ID
                                        --> TTY teletypewrite o teletipo, que es un dispositivo físco o virtual que permite
                                                interactuar con el sistema a nivel del kernel
                                        --> TIME medida de tiempo
                                        --> CMD nombre del proceso
                
                $ top                   --> muestra una interfaz con los procesos que se estan ejecutando más los recurso
                                            que consumen información adicional

                $ kill numero_PID       --> mata el proceso

                $ htop
                $ glandes