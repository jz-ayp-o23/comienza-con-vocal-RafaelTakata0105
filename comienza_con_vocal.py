"""
Tarea: Comienza con vocal
Author: Rafael Takata García
Fecha de entrega: 10/10/2023
Grupo: ESI-232B-5
Profesor: Jorge Adalberto Saldivar
"""

# Declaraciones
VOCALES = ["A", "Á", "E", "É", "I", "Í", "O", "Ó", "U", "Ú", "Ü"]
# Entradas
palabra = input("Escribe una palabra: ")
# Proceso
primer_letra = palabra[0]
if primer_letra.upper() in VOCALES:
    print(f"'{palabra}' comienza con vocal")
else:
    print(f"'{palabra}' no comienza con vocal")
# Salidas
