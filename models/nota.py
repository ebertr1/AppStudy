class Nota:
    def __init__(self) -> None:
        self.__id = 0
        self.__valor = 0
        self.__unidad = 0
        self.__cursa = 0
        self.__parametrosCalificacion = 0

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _valor(self):
        return self.__valor

    @_valor.setter
    def _valor(self, value):
        self.__valor = value

    @property
    def _unidad(self):
        return self.__unidad

    @_unidad.setter
    def _unidad(self, value):
        self.__unidad = value

    @property
    def _cursa(self):
        return self.__cursa

    @_cursa.setter
    def _cursa(self, value):
        self.__cursa = value

    @property
    def _parametrosCalificacion(self):
        return self.__parametrosCalificacion

    @_parametrosCalificacion.setter
    def _parametrosCalificacion(self, value):
        self.__parametrosCalificacion = value
        
    
    @property
    def serialize(self):
        return {
            'id': self.__id,
            'valor': self.__valor,
            'unidad': self.__unidad,
            'cursa': self.__cursa,
            'parametrosCalificacion': self.__parametrosCalificacion
        }
        
    def deserialize(self, data):
        self.__id = data['id']
        self.__valor = data['valor']
        self.__unidad = data['unidad']
        self.__cursa = data['cursa']
        self.__parametrosCalificacion = data['parametrosCalificacion']
        return self