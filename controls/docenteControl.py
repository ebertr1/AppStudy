from models.docente import Docente
from controls.tda.linked.linkedList import LinkedList
class DocenteControl():
    def __init(self):
        self.__docente = Docente()
        self.__lista = LinkedList()

    @property
    def _docente(self):
        return self.__docente

    @_docente.setter
    def _docente(self, value):
        self.__docente = value

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
        self._lista.add(self._docente, self._lista._length) 