
class Materia:
    def __init__(self):
        self.__id = 0
        self.__nombre = ''
        self.__ciclo = 0
        self.__descripcion = ''
        self.__cedulaDocente = ''

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
    def _ciclo(self):
        return self.__ciclo

    @_ciclo.setter
    def _ciclo(self, value):
        self.__ciclo = value

    @property
    def _descripcion(self):
        return self.__descripcion

    @_descripcion.setter
    def _descripcion(self, value):
        self.__descripcion = value

    @property
    def _cedula_docente(self):
        return self.__cedulaDocente

    @_cedula_docente.setter
    def _cedulaDocente(self, value):
        self.__cedulaDocente = value
        
    
    @property
    def serialize(self):
        return {
            'id': self.__id,
            'nombre': self.__nombre,
            'ciclo': self.__ciclo,
            'descripcion': self.__descripcion,
            'cedula_docente': self.__cedulaDocente
        }
    
    def deserializar(self, data):
        self.__id = data['id']
        self.__nombre = data['nombre']
        self.__ciclo = data['ciclo']
        self.__descripcion = data['descripcion']
        self.__cedulaDocente = data['cedula_docente']
        return self
