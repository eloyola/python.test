#set es una coleccion de elementos sin orden y no se puede repetir
personas = {'Juan', 'Pedro', 'Maria', 'Juan', 'Pedro', 'Maria'}
print(type(personas))
print('personas:', personas)

personas.add('Paco')
print('personas:', personas)


personas.remove('Paco')
print('personas:', personas)