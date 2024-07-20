from typing import Type
from controls.dao.daoAdapter import DaoAdapter
from models.docente import Docente
class DocenteDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Docente)
        self.__docente = None

    @property
    def _docente(self):
        if self.__docente is None:
            self.__docente = Docente()
        return self.__docente

    @_docente.setter
    def _docente(self, value):
        self.__docente = value

    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self.__docente._id = self._lista._length + 1
        self._save(self.__docente)