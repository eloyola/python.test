# OOP
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
    # methods
    # acciones o funciones

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad
# fin def de clase


coche = Coche()
coche.setColor ='Amarillo'
print(coche.marca, coche.getModelo(), coche.getColor())
print('velocidad actual', coche.getVelocidad())
coche.acelerar()
coche.acelerar()
print('velocidad actual', coche.getVelocidad())
