from models.parametros import Parametros
from controls.tda.linked.linkedList import LinkedList

class parametrosControl():
    def __init__(self):
        self.__parametros = Parametros()
        self.__lista = LinkedList()

    @property
    def _parametros(self):
        return self.__parametros

    @_parametros.setter
    def _parametros(self, value):
        self.__parametros = value

    @property
    def _lista(self):
        return self.__lista

    @_lista.setter
    def _lista(self, value):
        self.__lista = value

    @property
    def save(self):
        self._lista.add(self._parametros, self._lista._length)    