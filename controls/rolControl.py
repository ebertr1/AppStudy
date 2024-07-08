from models.rol import Rol
from controls.tda.linked.linkedList import LinkedList

class cuentaControl():
    def __init__(self):
        self.__rol = Rol()
        self.__lista = LinkedList()

    @property
    def _rol(self):
        return self.__rol

    @_rol.setter
    def _rol(self, value):
        self.__rol = value

    @property
    def _lista(self):
        return self.__lista

    @_lista.setter
    def _lista(self, value):
        self.__lista = value

    @property
    def save(self):
        self._lista.add(self._rol, self._lista._length)    
