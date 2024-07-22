import enum
class EnumTipoIdentificacion(enum.Enum):
    CEDULA = 'CEDULA'
    PASAPORTE = 'PASAPORTE'
    RUC = 'RUC'

    def getValue(self):
        return self.value