import sys
from controls.tda.linked.node import Node
from controls.exception.arrayPositionException import ArrayPositionException
from controls.exception.linkedEmpty import LinkedEmpty

class LinkedList(object):
    def __init__(self):
        self.__head = None
        self.__last = None
        self.__lenght = 0

    @property
    def _lenght(self):
        return self.__lenght

    @_lenght.setter
    def _lenght(self, value):
        self.__lenght = value

    @property
    def isEmpty(self):
        return self.__head == None or self.__lenght == 0
    
    def __addFirst__(self, data):
        if self.isEmpty:
            node = Node(data)
            self.__head = node
            self.__last = node
            self.__lenght += 1
        else:
            headold = self.__head
            node = Node(data, headold)
            self.__head = node
            self.__lenght += 1
    
    def __addLast__(self, data):
        if self.isEmpty:
            self.__addFirst__(data)
        else:
            node = Node(data)
            self.__last._next = node
            self.__last = node
            self.__lenght += 1

    def getNode(self, pos):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        elif pos < 0 or pos >= self._lenght:
            raise ArrayPositionException("Index out range")
        elif pos == 0:
            return self.__head
        elif pos == (self.__lenght - 1):
            return self.__last
        else:
            node = self.__head
            cont = 0
            while cont < pos:
                cont += 1
                node = node._next
            return node
    
    def add(self, data, pos = 0):
        if pos == 0:
            self.__addFirst__(data)
        elif pos == self.__lenght:
            self.__addLast__(data)
        else:
            node_preview = self.getNode(pos - 1)
            node_last = node_preview._next #self.getNode(pos)
            node = Node(data, node_last)
            node_preview._next = node
            self.__lenght += 1

    def edit(self, data, pos = 0):
        if pos == 0:
            self.__head._data = data 
        elif pos == self.__lenght:
            self.__last._data = data
        else:
            node = self.getNode(pos)  
            node._data = data

    def get(self, pos):
        try:
            return self.getNode(pos)._data
        except Exception as error:
            print(error)
            return None
        
    @property
    def clear(self):
        self.__head = None
        self.__last = None
        self.__lenght = 0

    def delete(self, pos = 0):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        elif pos < 0 or pos >= self._lenght:
            raise ArrayPositionException("Index out range")
        elif pos == 0:
            self.__head = self.__head._next
            self.__lenght -= 1
        elif pos == (self.__lenght - 1):
            node = self.getNode(pos - 1)
            node._next = None
            self.__last = node
            self.__lenght -= 1
        else:
            node_preview = self.getNode(pos - 1)
            node_last = node_preview._next
            node_preview._next = node_last._next
            self.__lenght -= 1 