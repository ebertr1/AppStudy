
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
    def serialize(self):
        return {
            'id': self.__id,
            'numeroCiclo': self.__numeroCiclo,
            'paralelo': self.__paralelo
        }   
        
    def deserialize(self, data):
        self.__id = data['id']
        self.__numeroCiclo = data['numeroCiclo']
        self.__paralelo = data['paralelo']
        return self
    
