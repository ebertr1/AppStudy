class Cuenta:
    def __init__(self):
        self.__correoInstitucional = ''
        self.__contrasenia = ''
        self.__id = 0


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
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

@property
def serialize(self):
    return {
        'correoInstitucional': self.__correoInstitucional,
        'contrasenia': self.__contrasenia,
        'id': self.__id
    }

def deserializar(self, data):
    self.__correoInstitucional = data['correoInstitucional']
    self.__contrasenia = data['contrasenia']
    self.__id = data['id']
    return self