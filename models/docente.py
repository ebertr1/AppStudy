from models.persona import Persona
class Docente (Persona):
    def __init__(self):
        super().__init__()
        self.__tituloAcademico = ''
        self.__cubiculo = 0
        self.__aniosExperiencia = 0

    @property
    def _tituloAcademico(self):
        return self.__tituloAcademico

    @_tituloAcademico.setter
    def _tituloAcademico(self, value):
        self.__tituloAcademico = value

    @property
    def _cubiculo(self):
        return self.__cubiculo

    @_cubiculo.setter
    def _cubiculo(self, value):
        self.__cubiculo = value

    @property
    def _aniosExperiencia(self):
        return self.__aniosExperiencia

    @_aniosExperiencia.setter
    def _aniosExperiencia(self, value):
        self.__aniosExperiencia = value

    @property
    def serialize(self):
        data = super().serialize
        data['tituloAcademico'] = self.__tituloAcademico
        data['cubiculo'] = self.__cubiculo
        data['aniosExperiencia'] = self.__aniosExperiencia
        return data

    def deserializar(self, data):
        super().deserializar(data)
        self.__tituloAcademico = data['tituloAcademico']
        self.__cubiculo = data['cubiculo']
        self.__aniosExperiencia = data['aniosExperiencia']
        return self
    