
class Ciclo:
    def __init__(self):
        self.__id = 0
        self.__numeroCiclo = ''
        self.__paralelo = 0


    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _numeroCiclo(self):
        return self.__numeroCiclo

    @_numeroCiclo.setter
    def _numeroCiclo(self, value):
        self.__numeroCiclo = value

    @property
    def _paralelo(self):
        return self.__paralelo

    @_paralelo.setter
    def _paralelo(self, value):
        self.__paralelo = value

    @property
    def serializable(self):
        return {
            "id": self._id,
            "numeroCiclo": self._numeroCiclo,
            "paralelo": self._paralelo
        }
    def deserializar(self, data):
        ciclo = Ciclo()
        ciclo._id = data['id']
        ciclo._numeroCiclo = data['numeroCiclo']
        ciclo._paralelo = data['paralelo']
        return ciclo
    

   