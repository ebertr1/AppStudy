class Cuenta:
    def __init__(self):
        self.__id = 0
        self.__correoInstitucional = ''
        self.__contrasenia = ''

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _correoInstitucional(self):
        return self.__correoInstitucional

    @_correoInstitucional.setter
    def _correoInstitucional(self, value):
        self.__correoInstitucional = value

    @property
    def _contrasenia(self):
        return self.__contrasenia

    @_contrasenia.setter
    def _contrasenia(self, value):
        self.__contrasenia = value
    
    @property
    def serializable(self):
        return {
            "id": self._id,
            "correoInstitucional": self._correoInstitucional,
            "contrasenia": self._contrasenia
        }
    def deserializar(self, data):
        cuenta = Cuenta()
        cuenta._id = data['id']
        cuenta._correoInstitucional = data['correoInstitucional']
        cuenta._contrasenia = data['contrasenia']
        return cuenta

    
