from typing import Type
from controls.tda.linked.linkedList import LinkedList
from controls.dao.daoAdapter import DaoAdapter
from models.malla import Malla

class MallaDaoControl(DaoAdapter):
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
        return self._list()
    
    @property
    def save(self):
        self.__malla._id = self._lista._length + 1
        self._save(self.__malla)  
        