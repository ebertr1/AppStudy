from models.persona import Persona
class Estudiante (Persona):
    def __init__(self):
        super().__init__()
        self.__numero_matricula = ''

    @property
    def _numero_matricula(self):
        return self.__numero_matricula

    @_numero_matricula.setter
    def _numero_matricula(self, value):
        self.__numero_matricula = value

    @property
    def serialize(self):
        data = super().serialize
        data['numero_matricula'] = self.__numero_matricula
        return data

    def deserializar(self, data):
        super().deserializar(data)
        self.__numero_matricula = data['numero_matricula']
        return self

    