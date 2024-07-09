class Asignacion:
    def __init__(self):
        self.__id = 0
        self.__cedulaDocente = ''
        self.__paralelo = ''
        self.__numeroIdentificacion = ''


    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _cedulaDocente(self):
        return self.__cedulaDocente

    @_cedulaDocente.setter
    def _cedulaDocente(self, value):
        self.__cedulaDocente = value

    @property
    def _paralelo(self):
        return self.__paralelo

    @_paralelo.setter
    def _paralelo(self, value):
        self.__paralelo = value

    @property
    def _numeroIdentificacion(self):
        return self.__numeroIdentificacion

    @_numeroIdentificacion.setter
    def _numeroIdentificacion(self, value):
        self.__numeroIdentificacion = value
@property
def serializable(self):
    return {
        'id': self.__id,
        'cedulaDocente': self.__cedulaDocente,
        'paralelo': self.__paralelo,
        'numeroIdentificacion': self.__numeroIdentificacion
    }

def deserializar(self, data):
    self.__id = data['id']
    self.__cedulaDocente = data['cedulaDocente']
    self.__paralelo = data['paralelo']
    self.__numeroIdentificacion = data['numeroIdentificacion']
    return self