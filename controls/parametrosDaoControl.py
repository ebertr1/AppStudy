from typing import Type
from controls.dao.daoAdapter import DaoAdapter
from models.parametros import Parametros

class ParametrosDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Parametros)
        self.__parametros= None

    @property
    def _parametros(self):
        if self.__parametros is None:
            self.__parametros = Parametros()
        return self.__parametros

    @_parametros.setter
    def _parametros(self, value):
        self.__parametros = value


    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self.__parametros._id = self._lista._length + 1
        self._save(self.__parametros)
