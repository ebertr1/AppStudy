class PeriodoAcademico:
    def __init__(self):
        self.__id = 0
        self.__fechaInicio = ''
        self.__fechaFinal = ''

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _fechaInicio(self):
        return self.__fechaInicio

    @_fechaInicio.setter
    def _fechaInicio(self, value):
        self.__fechaInicio = value

    @property
    def _fechaFinal(self):
        return self.__fechaFinal

    @_fechaFinal.setter
    def _fechaFin(self, value):
        self.__fechaFinal = value

    @property
    def serialize(self):
        return {
            'id': self.__id,
            'fechaInicio': self.__fechaInicio,
            'fechaFinal': self.__fechaFinal
        }
    
    def deserializar(self, data):
        PeriodoAcademico = PeriodoAcademico()
        PeriodoAcademico._id = data['id']
        PeriodoAcademico._fechaInicio = data['fechaInicio']
        PeriodoAcademico._fechaFinal = data['fechaFinal']
        return PeriodoAcademico