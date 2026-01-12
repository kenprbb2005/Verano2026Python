#calculadoraController.py

#logica, para que las funciones se ejecuten.
#que conecta el view y el model.

#como hacemos la conexion, importando
#     carpeta/archivo
#import model.calculadoraModell
from  model.calculadoraModell import calculadoraModell #este se usa cuando es una clase
import view.calculadoraView as _calculadoraView #este se usa cuando son solo funciones

#calculadoraController.py
class calculadoraController:
    
    def agregardatos(self, datoa, datob):
        _calculadoraModell = calculadoraModell(datoa, datob)
        return _calculadoraModell

    def presntardatos(self, _calculadoraModell):
        _calculadoraView.presntardatos(_calculadoraModell)

    def operaciones(self, _calculadoraModell, opcion):
        resultado = 0
        if opcion == 1:            
            resultado = calculadoraModell.sumar(_calculadoraModell)
            _calculadoraView.mostraResultado("suma", resultado)

        elif opcion == 2:            
            resultado = calculadoraModell.restar(_calculadoraModell)
            _calculadoraView.mostraResultado("resta", resultado)

        elif opcion == 3:            
            resultado = calculadoraModell.dividir(_calculadoraModell)
            _calculadoraView.mostraResultado("dividir", resultado)

        elif opcion == 4:            
            resultado = calculadoraModell.multiplicar(_calculadoraModell)
            _calculadoraView.mostraResultado("multiplicar", resultado)


        else:
            print("Opcion invalida")    



