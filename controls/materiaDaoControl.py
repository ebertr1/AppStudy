from controls.dao.daoAdapter import DaoAdapter
from models.materia import Materia

class MateriaControl(DaoAdapter):
    def __init__(self):
        super().__init__(Materia)
        self._materia = Materia()
    
    @property
    def materia(self):
        return self._materia
    
    @materia.setter
    def materia(self, value):
        self._materia = value
        
    @property
    def materias(self):
        return self._list()
    
    @property
    def save(self):
        self._materia._id = self._lista._length + 1
        self._lista.append(self._materia)