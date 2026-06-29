import platform
import socket
import getpass
import os

# Información básica del sistema
usuario = getpass.getuser()
hostname = socket.gethostname()
sistema = platform.system()
version = platform.version()
arquitectura = platform.machine()
procesador = platform.processor()

# Mostrar información
print("===================================")
print("        HOLA MUNDO PYTHON")
print("===================================")

print(f"Usuario       : {usuario}")
print(f"Hostname      : {hostname}")
print(f"Sistema       : {sistema}")
print(f"Versión       : {version}")
print(f"Arquitectura  : {arquitectura}")
print(f"Procesador    : {procesador}")

print("===================================")
print("Programa ejecutado correctamente")
print("===================================")

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
