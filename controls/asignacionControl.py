from models.asignacion import Asignacion
from controls.tda.linked.linkedList import LinkedList

class AsignacionControl():
    def __init__(self):
        self.__asignacion = Asignacion()
        self.__lista = LinkedList()

    @property
    def _asignacion(self):
        return self.__asignacion

    @_asignacion.setter
    def _asignacion(self, value):
        self.__asignacion = value

    @property
    def _lista(self):
        return self.__lista

    @_lista.setter
    def _lista(self, value):
        self.__lista = value

    @property
    def save(self):
        self._lista.add(self._asignacion, self._lista._length)    