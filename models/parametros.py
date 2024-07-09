class Parametros:
    def __init__(self):
        self.__id = 0
        self.__aprendizajeAutonomo = 0
        self.__evaluacionUnidad = 0
        self.__aprendizajeDocente = 0
        self.__aprendizajeExperimental = 0
        self.__lecciones = 0


    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _aprendizajeAutonomo(self):
        return self.__aprendizajeAutonomo

    @_aprendizajeAutonomo.setter
    def _aprendizajeAutonomo(self, value):
        self.__aprendizajeAutonomo = value

    @property
    def _evaluacionUnidad(self):
        return self.__evaluacionUnidad

    @_evaluacionUnidad.setter
    def _evaluacionUnidad(self, value):
        self.__evaluacionUnidad = value

    @property
    def _aprendizajeDocente(self):
        return self.__aprendizajeDocente

    @_aprendizajeDocente.setter
    def _aprendizajeDocente(self, value):
        self.__aprendizajeDocente = value

    @property
    def _aprendizajeExperimental(self):
        return self.__aprendizajeExperimental

    @_aprendizajeExperimental.setter
    def _aprendizajeExperimental(self, value):
        self.__aprendizajeExperimental = value

    @property
    def _lecciones(self):
        return self.__lecciones

    @_lecciones.setter
    def _lecciones(self, value):
        self.__lecciones = value

    @property
    def serializable(self):
        return {
            "id": self._id,
            "aprendizajeAutonomo": self._aprendizajeAutonomo,
            "evaluacionUnidad": self._evaluacionUnidad,
            "aprendizajeDocente": self._aprendizajeDocente,
            "aprendizajeExperimental": self._aprendizajeExperimental,
            "lecciones": self._lecciones
        }
    def deserializar(self, data):
        parametros = Parametros()
        parametros._id = data['id']
        parametros._aprendizajeAutonomo = data['aprendizajeAutonomo']
        parametros._evaluacionUnidad = data['evaluacionUnidad']
        parametros._aprendizajeDocente = data['aprendizajeDocente']
        parametros._aprendizajeExperimental = data['aprendizajeExperimental']
        parametros._lecciones = data['lecciones']
        return parametros
    

       