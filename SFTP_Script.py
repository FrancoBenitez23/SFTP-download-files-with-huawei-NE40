from threading import local
import paramiko
import time 


#abrir un transport
host, port = "192.168.1.82", 22
transport = paramiko.Transport((host, port))
#abrir un cliente
ssh_open = paramiko.SSHClient()
ssh_open.load_system_host_keys()
ssh_open.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_open.connect("192.168.1.82",22,"franco","Ninguna123-")

#Authentication
username, password = "franco", "Ninguna123-"
transport.connect(None, username, password)

#mandale mecha
sftp = paramiko.SFTPClient.from_transport(transport)

#se envia comando
comando = ssh_open.invoke_shell()
comando.send("N\n")
time.sleep(6)
comando.send("sys\n")
time.sleep(6)
comando.send("display acl all >> texto.txt\n")
time.sleep(6)
output = comando.recv(65535) 

remotepath ="texto.txt"
localpath = "texto.txt"
sftp.get(remotepath,localpath)

#close 
if sftp: sftp.close()
if transport: transport.close()
