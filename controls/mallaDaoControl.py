from typing import Type
from controls.tda.linked.linkedList import Linked_List
from controls.dao.daoAdapter import DaoAdapter
from models.malla import Malla

class MallaDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Malla)
        self.__malla = None

    @property
    def _malla(self):
        if self.__malla is None:
            self.__malla = Malla()
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
<<<<<<< HEAD
        self._save(self.__malla)  
        
=======
        self._save(self.__malla)
>>>>>>> main
