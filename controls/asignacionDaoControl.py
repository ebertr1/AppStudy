from typing import Type
from controls.dao.daoAdapter import DaoAdapter
from models.asignacion import Asignacion

class AsignacionDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Asignacion)
        self.__asignacion = None

    @property
    def _asignacion(self):
        if self.__asignacion is None:
            self.__asignacion = Asignacion()
        return self.__asignacion

    @_asignacion.setter
    def _asignacion(self, value):
        self.__asignacion = value


    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self.__asignacion._id = self._lista._length + 1
        self._save(self.__asignacion)
