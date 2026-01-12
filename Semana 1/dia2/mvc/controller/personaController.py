from model.personaModel import personaModel
import view.personaView as _personaView

class personaController:
    def crearPersona(self, nombre, edad, genero):
        _personaModel = personaModel(nombre, edad, genero)
        print("Persona creada")
        return _personaModel
    
    def mostrarDatos(self, _personaModel):
        _personaView.mostrarDatos(_personaModel)
