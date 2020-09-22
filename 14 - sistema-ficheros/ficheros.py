from io import open
import pathlib
import shutil
import os
"""
#abrir archivo
path = str(pathlib.Path().absolute()) + '/texto.txt'
#print(path)
archivo = open(path, 'a+')

#escribir
archivo.write('****** texto metido desde python **********\n')

#cerrar
archivo.close()

#abrir archivo
path = str(pathlib.Path().absolute()) + '/texto.txt'
archivo = open(path, 'r')
#leer contenido
#contenido = archivo.read()
#print(contenido)

#leer y guardarlo en lista
lista = archivo.readlines()
archivo.close()

for elemento in lista:
    print(elemento.upper())
"""
#copiar
ruta_original = str(pathlib.Path().absolute()) + '/texto.txt'
ruta_nueva = str(pathlib.Path().absolute()) + '/texto_copiado.txt'
shutil.copyfile(ruta_original, ruta_nueva)

#mover
#shutil.mover(ruta_original, ruta_nueva)

#eliminar
#os.remove(ruta_nueva)

#comprobar is existe
import os.path
ruta_comprobar = os.path.abspath('./') + '/texto_copiado.txt'
print(ruta_comprobar)
#print(os.path.abspath('./'))
if os.path.isfile(ruta_comprobar):
    print('fichero existe')
else:
    print('fichero no existe')