from models.estudiante import Estudiante
from controls.tda.linked.linkedList import LinkedList
class EstudianteControl():
    def __init(self):
        self.__estudiante = Estudiante()
        self.__lista = LinkedList()

    @property
    def _estudiante(self):
        return self.__estudiante

    @_estudiante.setter
    def _estudiante(self, value):
        self.__estudiante = value

    @property
    def _lista(self):
        return self.__lista

    @_lista.setter
    def _lista(self, value):
        self.__lista = value


    

    @_lista.setter
    def _lista(self, value):
        self.__lista = value

    @property
    def save(self):
        self._lista.add(self._estudiante, self._lista._length) 

   
