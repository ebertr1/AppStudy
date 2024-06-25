from controls.tda.linked.linkedList import LinkedList
from controls.exception.linkedEmptyException import LinkedEmpty

class StackOperation (LinkedList):
    def __init__(self, tope):
        self.__tope = tope

    @property
    def _tope(self):
        return self.__tope

    @_tope.setter
    def _tope(self, value):
        self.__tope = value

    @property
    def verifyTope (self):
        return self._length < self._tope
    
    def push(self, data):
        if self.verifyTope:
            self.__addFirst__(data)
        else:
            raise LinkedEmpty("Stack is full")
        
    @property
    def pop(self):
        if self.isEmpty:
            raise LinkedEmpty("Stack is empty")
        else: 
            return self.delete(0)
        
    @property
    def print(self):
        print('Elementos:')
        current = self._head 
        while current is not None:
            print(current._data)
            current = current._next