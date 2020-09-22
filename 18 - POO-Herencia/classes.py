class Persona:
    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def getApellidos(self):
        return self.apellidos

    def hablar(self):
        return 'estoy hablando'


class Informatico(Persona):
    def __init__(self):
        self.lenguajes = 'html, css, javascript, php'
        self.experiencia = 5

    def getLenguajes(self):
        return self.lenguajes

    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes

    def programar(self):
        return 'estoy programando'


class TecnicoRedes(Informatico):
    def __init__(self):
        #llamando a constructor de clase padre
        super().__init__()
        self.experiencia=15
        self.auditoriaRedes='experto'
    def setSalario(self, salario):
        self.salario = salario

    def getSalario(self):
        return self.salario
