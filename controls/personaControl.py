from models.persona import Persona
from controls.tda.linked.linkedList import LinkedList
class PersonaControl():
    def __init(self):
        self.__persona = Persona()
        self.__lista = LinkedList()

    @property
    def _persona(self):
        return self.__persona

    @_persona.setter
    def _persona(self, value):
        self.__persona = value

    @property
    def _lista(self):
        return self.__lista

    @_lista.setter
    def _lista(self, value):
        self.__lista = value
    
    @property
    def save(self):
        self._lista.add(self._persona, self._lista._length) 