from controls.tda.linked.linkedList import LinkedList
from models.materia import Materia

class MateriaControl():
    def __init__(self):
        self._materia = Materia()
        self._lista = LinkedList()
    
    @property
    def materia(self):
        return self._materia
    
    @materia.setter
    def materia(self, value):
        self._materia = value
        
    @property
    def _lista(self):
        return self.__lista

    @_lista.setter
    def _lista(self, value):
        self.__lista = value

    @property
    def save(self):
        self._lista.add(self._materia, self._lista._length)    
