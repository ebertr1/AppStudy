class Malla:
    def __init__(self):
        self.__id = 0
        self.__nombre = ''
        self.__descripcion = ''
        self.__fechaCreacion = ''

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
    def _fechaCreacion(self):
        return self.__fechaCreacion

    @_fechaCreacion.setter
    def _fechaCreacion(self, value):
        self.__fechaCreacion = value

    @property
    def serializable(self):
        return {
            "id": self._id,
            "nombre": self._nombre,
            "descripcion": self._descripcion,
            "fechaCreacion": self._fechaCreacion
        }
    def deserializar(self, data):
        malla = Malla()
        malla._id = data['id']
        malla._nombre = data['nombre']
        malla._descripcion = data['descripcion']
        malla._fechaCreacion = data['fechaCreacion']
        return malla
    

       