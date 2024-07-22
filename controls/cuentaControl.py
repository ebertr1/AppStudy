from models.cuenta import Cuenta
from controls.tda.linked.linkedList import LinkedList

class cuentaControl():
    def __init__(self):
        self.__cuenta = Cuenta()
        self.__lista = LinkedList()

    @property
    def _cuenta(self):
        return self.__cuenta

    @_cuenta.setter
    def _cuenta(self, value):
        self.__cuenta = value

    @property
    def _lista(self):
        return self.__lista

    @_lista.setter
    def _lista(self, value):
        self.__lista = value

    @property
    def save(self):
        self._lista.add(self._cuenta, self._lista._length)    
