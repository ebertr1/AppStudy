from models.ciclo import Ciclo
from controls.tda.linked.linkedList import LinkedList

class cicloControl():
    def __init__(self):
        self.__ciclo = Ciclo()
        self.__lista = LinkedList()

    @property
    def _ciclo(self):
        return self.__ciclo

    @_ciclo.setter
    def _ciclo(self, value):
        self.__ciclo = value

    @property
    def _lista(self):
        return self.__lista

    @_lista.setter
    def _lista(self, value):
        self.__lista = value

    @property
    def save(self):
        self._lista.add(self._ciclo, self._lista._length)    
