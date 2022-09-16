# SFTP-download-files-with-huawei-NE40
"""Aclaracion"""
Los comandos ejecutados del script funcionan en otros routers de la marca con la misma version de software.

Español:
El script funciona de la siguiente manera: 
Se crea una coneccion con el servidor ssh corriendo en el router NE40, se envian los comandos sobre una "shell" inicializada, como se ve en la linea:

comando = ssh_open.invoke_shell()

sobre esta shell, que se encuentra en la variable "comando" se van a ir ejecutando los comandos sobre el router. Esta es toda la logica principal del script, la aplicacion del sftp arranca en la linea 34: 

sftp.get(remotepath,localpath)

En donde se descarga un archivo generado dentro del router, donde se encuentra un display de las acl creadas en el router.
