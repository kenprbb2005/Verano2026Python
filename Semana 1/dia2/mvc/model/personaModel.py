class personaModel:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def mostrarDatos(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Genero: {self.genero}"