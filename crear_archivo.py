# todo archivo se tiene que crear y cerrar
# Puedes usar diferentes modos al abrir un archivo:
# "w": Escribe y crea un archivo. Sobrescribe si ya existe.
# "a": Escribe al final del archivo (append), sin sobrescribir el contenido existente.
# "r": Abre el archivo solo para lectura.
# "x": Crea un archivo, pero genera un error si ya existe.
# "wb", "rb": Modos para escribir/leer archivos binarios.

archivo = open('texto.XLS','w') # Abriendo y creando 
archivo.write('teste de prueba')
archivo.close() # Cerrar


import json

# # Escribir JSON
datos = {"nombre": "Juan", "edad": 30, "ocupacion": "Ingeniero"}
with open("datos.json", "w") as archivo:
    json.dump(datos, archivo, indent=4)

# # Leer JSON
with open("datos.json", "r") as archivo:
    datos_cargados = json.load(archivo)
    print(datos_cargados)

import csv

# Escribir CSV
with open("datos.csv", "w", newline="") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["Nombre", "Edad", "Ocupación"])
    escritor.writerow(["Ana", 25, "Doctora"])
    escritor.writerow(["Luis", 28, "Profesor"])

# Leer CSV
with open("datos.csv", "r") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)


# Escribir datos binarios
data = b"Este es un ejemplo de datos binarios."
with open("binario.bin", "wb") as archivo:
    archivo.write(data)

# Leer datos binarios
with open("binario.bin", "rb") as archivo:
    contenido_binario = archivo.read()
    print(contenido_binario)


# Leer contenido de un archivo en una carpeta
with open('ruta_archivo', "r") as archivo:
    contenido = archivo.read()
    print(contenido)


# Crear un archivo en una ruta especifica 

import os

# # Definir ruta
carpeta = "mi_carpeta"
os.makedirs(carpeta, exist_ok=True)  # Crear la carpeta si no existe

# # Crear archivo dentro de la carpeta
ruta_archivo = os.path.join(carpeta, "archivo.txt")
with open(ruta_archivo, "w") as archivo:
    archivo.write("Este archivo está en una carpeta específica.")


# Revisar si una carpeta o archivo existe
if os.path.exists(ruta_archivo):
    print("El archivo existe.")
else:
    print("El archivo no existe.")
