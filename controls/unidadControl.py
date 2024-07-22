from models.unidad import Unidad
from controls.tda.linked.linkedList import LinkedList

class unidadControl():
    def __init__(self):
        self.__unidad = Unidad()
        self.__lista = LinkedList()

    @property
    def _unidad(self):
        return self.__unidad

    @_unidad.setter
    def _unidad(self, value):
        self.__unidad = value

    @property
    def _lista(self):
        return self.__lista

    @_lista.setter
    def _lista(self, value):
        self.__lista = value

    @property
    def save(self):
        self._lista.add(self._unidad, self._lista._length)    
