from controls.dao.daoAdapter import DaoAdapter
from models.ciclo import Ciclo

class CicloControl(DaoAdapter):
    def __init__(self):
        def __init__(self):
            super().__init__(Ciclo)
            self._ciclo = Ciclo()
    
    @property
    def ciclo(self):
        return self._ciclo
    
    @ciclo.setter
    def ciclo(self, value):
        self._ciclo = value
        
    @property
    def ciclos(self):
        return self._ciclos()
    
    @property
    def _save(self):
        self.__ciclo._id = self._lista._length + 1
        self._lista.append(self.__ciclo)