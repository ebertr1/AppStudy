
from models.enumTipoIdentificacion import EnumTipoIdentificacion
class Asignacion:
    def __init__(self):
        self.__id = 0
        self.__cedulaDocente = ''
        self.__paralelo = ''
        self.__tipoIdentificacion = EnumTipoIdentificacion

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
    def _tipoIdentificacion(self):
        return self.__tipoIdentificacion

    @_tipoIdentificacion.setter
    def _tipoIdentificacion(self, value):
        self.__tipoIdentificacion = value

    @property
    def serializable(self):
        return {
            "id": self._id,
            "cedulaDocente": self._cedulaDocente,
            "paralelo": self._paralelo,
            "tipoIdentificacion": self._tipoIdentificacion.__str__()
        }
    
    def deserializar(self, data):
        asignacion = Asignacion()
        asignacion._id = data['id']
        asignacion._cedulaDocente = data['cedulaDocente']
        asignacion._paralelo = data['paralelo']
        asignacion._tipoIdentificacion = data['tipoIdentificacion']
        return asignacion
    
