from typing import Type
from controls.dao.daoAdapter import DaoAdapter
from models.estudiante import Estudiante
class EstudianteDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Estudiante)
        self.__estudiante = None

    @property
    def _estudiante(self):
        if self.__estudiante is None:
            self.__estudiante = Estudiante()
        return self.__estudiante

    @_estudiante.setter
    def _estudiante(self, value):
        self.__estudiante = value


    
    
    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self.__estudiante._id = self._lista._length + 1
        self._save(self.__estudiante)

        