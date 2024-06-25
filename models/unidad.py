class Unidad:
     def __init__(self):
        self.__id = 0
        self.__numeroUnidad = 0
        self.__duracionSemanas = 0

        @property
        def _id(self):
            return self.__id

        @_id.setter
        def _id(self, value):
            self.__id = value

        @property
        def _numeroUnidad(self):
            return self.__numeroUnidad

        @_numeroUnidad.setter
        def _numeroUnidad(self, value):
            self.__numeroUnidad = value

        @property
        def _duracionSemanas(self):
            return self.__duracionSemanas

        @_duracionSemanas.setter
        def _duracionSemanas(self, value):
            self.__duracionSemanas = value

        
@property
def serialize(self):
    return {
        'id': self.__id,
        'numeroUnidad': self.__numeroUnidad,
        'duracionSemanas': self.__duracionSemanas
    }

def deserializar(self, data):
    self.__id = data['id']
    self.__numeroUnidad = data['numeroUnidad']
    self.__duracionSemanas = data['duracionSemanas']
    return self
