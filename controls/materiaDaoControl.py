from models.materia import Materia
from controls.dao.daoAdapter import DaoAdapter
from controls.tda.linked.linkedList import LinkedList

class materiaDaoControl(DaoAdapter):
    def __init__(self):
        self.__materia = Materia()
        self.__lista = LinkedList()

    @property
    def _materia(self):
        return self.__materia

    @_materia.setter
    def _materia(self, value):
        self.__materia = value

    @property
    def _lista(self):
        return self.__lista

    @_lista.setter
    def _lista(self, value):
        self.__lista = value

    @property
    def save(self):
        self.__materia._id = self._lista._length + 1
        self._save(self.__materia)  