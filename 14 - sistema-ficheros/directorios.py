import os, shutil

#crear carpeta
if not os.path.isdir('./mi_carpeta'):
    os.mkdir('./mi_carpeta')
else:
    print('directorio ya existe')

#eliminar
# os.rmdir('./mi_carpeta')

#copiar
# ruta_original = './mi_carpeta'
# ruta_nueva = './mi_carpeta_copiada'
# shutil.copytree(ruta_original, ruta_nueva)

print('contenido de carpeta')
contenido = os.listdir('./mi_carpeta')
for fichero in contenido:
    print(fichero)