class Rol:
    def __init__(self):
        self.__id = 0
        self.__nombre = ''
        self.__descripcion = ''

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _descripcion(self):
        return self.__descripcion

    @_descripcion.setter
    def _descripcion(self, value):
        self.__descripcion = value

@property
def serialize(self):
    return {
        'id': self.__id,
        'nombre': self.__nombre,
        'descripcion': self.__descripcion
    }

def deserializar(self, data):
    self.__id = data['id']
    self.__nombre = data['nombre']
    self.__descripcion = data['descripcion']
    return self