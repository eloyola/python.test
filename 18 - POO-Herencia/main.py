import classes
persona = classes.Persona()
persona.setNombre('Paco')
print(persona.getNombre())

informatico = classes.Informatico()
informatico.setNombre('Carlos')
print(informatico.getNombre())

tecnico = classes.TecnicoRedes()
tecnico.setNombre('Mateo')
print(tecnico.getNombre(), tecnico.getLenguajes())