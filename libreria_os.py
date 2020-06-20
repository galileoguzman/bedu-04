# importar biblioteca
import os

files = os.listdir()
# print(type(files))
# print(files)

for f in files:
    file_size = os.path.getsize(f)
    print(f'The file {f} is {file_size}')


'''
tarea_os_archivos.py
----------------------------------------
lista_de_archivos.py...............  135
readme.md.......................... 1141
modulos.py.........................  412
----------------------------------------
'''
