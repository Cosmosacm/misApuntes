# **Comandos Básicos CMD**

Shell de línea de comandos.  

      C:\> cls			limpiar pantalla

      C:\> ipconfig		validar a que ip de la red se conecta
		validar si el dhcp esta asignando direccionamiento

C:\> telnet

## ** Funcionalidades netstat **  


	C:\> netstat -a

	C:\> eventvwr		# abre el visor de eventos de Windows también tecla windows+R digita eventvwr


Tener en cuenta la fecha y hora del reporte del incidente, y los 4 ítem incluidos en el registro de Windows (Aplicación; faltantes Seguridad, instalación y sistema)



inicio / panel de control / programas / activar y desactivar las caracteristicas de windows / se selecciona telnet



	*** Funcionalidades Netsh ***

   utilidad que permite mostrar o modificar la configuración de red de un equipo. Se puede usar en archivos por lotes o scripts.
   https://docs.microsoft.com/es-es/windows-server/networking/technologies/netsh/netsh-contexts


C:\> netsh ?


   Validar datos de la interfaz de red wlan o lan en uso

C:\> netsh wlan show interface


   validar redes almacenadas en la interfaz wlan
	
C:\> netsh wlan show profile


   identificar contraseñas de redes wifi

C:\> netsh wlan show profile name="nombre_red" key=clear




	*** Funcionalidades DNS ***


   Borrar cache DNS

C:\> ipconfig /flushdns		* Si se ha ejecutado correctamente aparece
					* "Se vació con exito la caché de resolución de DNS"

### **nslookup**  

       C:\> nslookup

Averiguar IP pública externa

      :\> nslookup myip.opendns.com resolver1.opendns.com

### **sfc**  

      C:\WINDOWS\system32>sfc /verifyonly

      C:\Windows>sfc /scannow
