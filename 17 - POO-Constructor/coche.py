# definition (molde para crear mas obj de ese tipo)
class Coche:
    # attr o prop (vars)
    # caracteristicas de clase
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    caballaje = 500
    velocidad = 300
    plazas = 2

    # visibilidad
    soy_publico = 'Hola soy un attr publico'
    __soy_privado = 'attr privada'
    # methods
    # acciones o funciones

    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas

    def getPrivado(self):
        return self.__soy_privado

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def setMarca(self, marca):
        self.marca = marca

    def getMarca(self):
        return self.marca

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad

    def getInfo(self):
        info = '------info del coche -------'
        info += f'\n Color {self.getColor()}'
        info += f'\n Marca {self.getMarca()}'
        info += f'\n Modelo {self.getModelo()}'
        info += f'\n Velocidad {self.getVelocidad()}'
        return info
# fin def de clase