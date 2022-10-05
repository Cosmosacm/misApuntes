# OpenSSH  

Validar si los servicios **openSSH-client** y **openSSH-server** están instalados:

    PS C:\> Get-WindowsCapability -Online | ? Name -like 'OpenSSH*'  

    1. Abrir Configuraciones (Settings)
    2. Seleccionar Aplicaciones (Apps)
    3. Características opcionales (optional feactures)


Validar estatus de los puertos abiertos

    PS C:\> nestat -ano  

