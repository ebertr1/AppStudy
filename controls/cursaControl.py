from models.cursa import Cursa
from controls.tda.linked.linkedList import LinkedList

class cursaControl():
    def __init__(self):
        self.__cursa = Cursa()
        self.__lista = LinkedList()

    @property
    def _cursa(self):
        return self.__cursa

    @_cursa.setter
    def _cursa(self, value):
        self.__cursa = value

    @property
    def _lista(self):
        return self.__lista

    @_lista.setter
    def _lista(self, value):
        self.__lista = value

    @property
    def save(self):
        self._lista.add(self._cursa, self._lista._length)    
