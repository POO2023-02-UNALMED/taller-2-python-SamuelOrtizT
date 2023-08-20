class Asiento:
    def __init__ (self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    def cambiarColor(self, color):
        if color in ["rojo", "verde", "amarillo", "negro", "blanco,"]:
            self.color = color
class Motor:
    def __init__ (self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    def cambiarRegistro(self, registro):
        self.registro = registro
    def asignarTipo(self, tipo):
        if tipo in ["electrico", "gasolina"]:
            self.tipo = tipo
class Auto:
    cantidadCreados = 0
    def __init__ (self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        Auto.cantidadCreados += 1
    def cantidadAsientos(self):
        x = 0
        for asiento in self.asientos:
            if type(asiento) == Asiento:
                x += 1
        return x
    def verificarIntegridad(self):
        x = 0
        for asiento in self.asientos:
            if type(asiento) == Asiento and asiento.registro == self.motor.registro:
                x += 1
        y = self.cantidadAsientos()
        if x == y:
            return "Auto original"
        else:
            return "Las piezas no son originales"
