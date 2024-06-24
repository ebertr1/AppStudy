from controls.dao.daoAdapter import DaoAdapter
from models.periodoAcademico import PeriodoAcademico

class PeriodoAcademicoControl(DaoAdapter):
    def __init__(self):
        super().__init__(PeriodoAcademico)
        self.__periodoAcademico = PeriodoAcademico()
    
    @property
    def periodoAcademico(self):
        return self.__periodoAcademico
    
    @periodoAcademico.setter
    def periodoAcademico(self, value):
        self.__periodoAcademico = value
        
    @property
    def periodosAcademicos(self):
        return self._list()
    
    @property
    def save(self):
        self.__periodoAcademico._id = self._lista._length + 1
        self._lista.append(self.__periodoAcademico)