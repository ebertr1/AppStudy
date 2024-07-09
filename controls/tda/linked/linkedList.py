from controls.tda.linked.nodo import Node
from controls.exception.arrayPositionException import ArrayPositionException
from controls.exception.linkedEmptyException import LinkedEmpty


class LinkedList (object):
    def __init__(self):
        self.__head = None
        self.__last = None
        self.__length = 0
        
    @property
    def _head(self):
        return self.__head

    @_head.setter
    def _head(self, value):
        self.__head = value

    @property
    def _length(self):
        return self.__length

    @_length.setter
    def _length(self, value):
        self.__length = value


    @property 
    def isEmpty(self):
        return self.__head == None or self.__length == 0
    

    def __addFirst__(self, data):
        if self.isEmpty:
            node = Node(data)
            self.__head = node
            self.__last = node
            self.__length += 1
        else:
            headOld = self.__head
            node = Node(data, headOld)
            self.__head = node
            self.__length += 1


    def __addLast__(self, data):
        if self.isEmpty:
            self.__addFirst__(data)
        else:
            node = Node(data)
            self.__last._next = node
            self.__last = node
            self.__length += 1
               
    @property
    def clear(self):
        self.__head = None
        self.__last = None
        self.__length = 0
        

    def add(self, data, pos = 0):
        if pos == 0:
            self.__addFirst__(data)
        elif pos == self.__length:
            self.__addLast__(data)
        else:       
            node_preview = self.getNode(pos - 1)
            node_last = node_preview._next
            node = Node(data, node_last)
            node_preview._next = node
            self.__length += 1  
    
    def edit(self, data, pos):
        if pos == 0:
            self.__head._data = data
        elif pos == self.__length:
            self.__last._data = data
        else:
            node = self.getNode(pos)
            node._data = data   
    
    
    #esto no tiene el ing pero si te sirve bueno es el toArray y el delete
    @property
    def toArray(self):
        if self.isEmpty:
            return []
        else:
            array = []
            node = self.__head
            while node != None:
                array.append(node._data)
                node = node._next
            return array
        

    def delete(self, pos):
        if pos == 0:
            self.__head = self.__head._next
        elif pos == self.__length - 1:
            node = self.__head
            while node._next != self.__last:
                node = node._next
            node._next = None
            self.__last = node
        else:
            cont = 1
            node = self.__head
            while node._next != None and cont < pos:
                node = node._next
                cont += 1
            node._next = node._next._next
        self.__length -= 1
    
                     
    def getNode(self, pos):
        if self.isEmpty:
            raise LinkedEmpty("List Empty")
        elif pos < 0 or pos >= self._length:
            raise ArrayPositionException("Index out of range")
        elif pos == 0:
            return self.__head
        elif pos == (self.__length - 1):
            return self.__last
        else:
            node = self.__head
            cont = 0
            while cont < pos:
                cont += 1
                node = node._next
            return node
    
        
 
 
    def get(self, pos):
        if self.isEmpty:
            raise LinkedEmpty("List Empty")
        elif pos < 0 or pos >= self._length:
            raise ArrayPositionException("Index out of range")
        elif pos == 0:
            return self.__head._data
        elif pos == (self.__length - 1):
            return self.__last._data
        else:
            node = self.__head
            cont = 0
            while cont < pos:
                cont += 1
                node = node._next
            return node._data
    
    def __str__(self) -> str:
        out = ""
        if self.isEmpty:
            out = "List is Empty"
        else:
            node = self.__head
            while node != None:
                out += str(node._data)
                node = node._next
        return out
    
    @property
    def print(self):
        node = self.__head
        data = ""
        while node != None:
                data += str(node._data)+"    "
                node = node._next
        print("Lista de Datos")
        print(data)