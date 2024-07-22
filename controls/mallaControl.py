from models.malla import Malla
from controls.tda.linked.linkedList import LinkedList

class mallaControl():
    def __init__(self):
        self.__malla = Malla()
        self.__lista = LinkedList()

    @property
    def _malla(self):
        return self.__malla

    @_malla.setter
    def _malla(self, value):
        self.__malla = value

    @property
    def _lista(self):
        return self.__lista

    @_lista.setter
    def _lista(self, value):
        self.__lista = value

    @property
    def save(self):
        self._lista.add(self._malla, self._lista._length)    
