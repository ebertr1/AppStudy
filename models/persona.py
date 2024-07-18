class Persona:
    def __init__(self):
        self.__id=0
        self.__nombre= ''
        self.__apellido=''
        self.__direccion= ''

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
    def _apellido(self):
        return self.__apellido

    @_apellido.setter
    def _apellido(self, value):
        self.__apellido = value

    @property
    def _dirección(self):
        return self.__direccion

    @_dirección.setter
    def _dirección(self, value):
        self.__direccion = value
        
    @property
    def serializable(self):
        return {
            'id': self.__id,
            'nombre': self.__nombre,
            'apellido': self.__apellido,
            'direccion': self.__direccion
        }   
        
    def deserializar(self, data):
        self.__id = data['id']
        self.__nombre= data['nombre']
        self.__apellido = data['apellido']
        self.__direccion = data['direccion']
        return self

        