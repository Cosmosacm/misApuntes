# OpenSSH  

Validar si los servicios **openSSH-client** y **openSSH-server** están instalados:

    PS C:\> Get-WindowsCapability -Online | ? Name -like 'OpenSSH*'  

Validar estatus de los puertos abiertos

    PS C:\> nestat -ano  

