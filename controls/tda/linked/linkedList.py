import sys
from controls.tda.linked.node import Node
from controls.exception.arrayPositionException import ArrayPositionException
from controls.exception.linkedEmpty import LinkedEmpty

from numbers import Number
from controls.tda.linked.ordenacion.shellSort import ShellSort
from controls.tda.linked.ordenacion.quickSort import QuickSort
from controls.tda.linked.ordenacion.mergeSort import MergeSort
from controls.tda.linked.busqueda.binary import Binary
from controls.tda.linked.busqueda.binarySecuencial import BinarySecuencial
from controls.tda.linked.busqueda.secuencial import Secuencial

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
        
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        elif pos < 0 or pos >= self._lenght:
            raise ArrayPositionException("Index out range")
        elif pos == 0:
            return self.__head._data
        elif pos == (self.__lenght - 1):
            return self.__last._data
        else:
            node = self.__head
            cont = 0
            while cont < pos:
                cont += 1
                node = node._next
            return node._data
        
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
    
    #funcion para conocer el almacenamiento de la lista
    @property
    def _lenghtLista_(self):
        lenght = sys.getsizeof(self.__head) + sys.getsizeof(self.__last) + sys.getsizeof(self.__lenght)
        node_lenght = sys.getsizeof(Node) 
        lenght += node_lenght * self.__lenght
        return lenght





    def _get(self, id):
        list = self._list()
        array = list.toArray
        for i in range(0, len(array)):
            if array[i]._id == id:
                return array[i]
        return None





    #Convierte una lista a un array -------------------------------------------------------------------------------------------
    @property
    def toArray(self):
        array = []
        if not self.isEmpty:
            node = self.__head
            cont = 0
            while cont < self._lenght:
                array.append(node._data)
                cont += 1
                node = node._next
        return array
    #Convierte un array a una lista -------------------------------------------------------------------------------------------
    def toList(self, array):
        self.clear
        for i in range (0, len(array)):
            self.__addLast__(array[i])

    #Ordenamiento de la lista-------------------------------------------------------------------------------------------------
    def sort(self, type, metodo = 1):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            if isinstance(array[0], Number) or isinstance(array[0], str):
                if metodo == 1:
                    order = QuickSort()
                elif metodo == 2:
                    order = MergeSort()
                else:
                    order = ShellSort()
                if type == 1:
                    array = order.sort_primitive_ascendent(array)
                else:
                    array = order.sort_primitive_descendent(array)
            self.toList(array)

    def sort_models(self, attribute, type = 1, metodo = 1):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            if isinstance(array[0], object):
                if metodo == 1:
                    order = QuickSort()
                elif metodo == 2:
                    order = MergeSort()
                else:
                    order = ShellSort()
                if type == 1:
                    array = order.sort_models_ascendent(array, attribute)
                else:
                    array = order.sort_models_descendent(array, attribute)
            
            self.toList(array)
        return self


    #---------------BUSQUEDA SECUENCIAL-----------------------------------------------------------------------------------------------------------

    def search_equals(self, data):
        list = LinkedList()
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            for i in range(0, len(array)):
                if array[i].lower().startswith(data.lower()): #array[i] == data:
                    list.add(array[i], list._length)
        return list

    def search_equals_number(self, number):
        list = LinkedList()
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            for i in range(len(array)):
                if array[i] == number:
                    list.add(array[i], list._lenght)
        #imprimir el numero de ocurrencia que se encontraron
        #print(f"El número {number} fue encontrado {list._lenght} veces")
        return list

    

    
    def search_binary(self, element):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            search = Binary()
            index = search.search_binary(array, element)
            if index == -1:
                print(f"Elemento {element} no encontrado")
            else:
                print(f"Elemento {element} encontrado en el índice: {index}")
        
        self.toList(array)
        return self

    def search_binary_models(self, element, attribute):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            search = Binary()
            index = search.search_binary_models(array, element, attribute)
            if index == -1:
                print(f"Models con {attribute} = {element} no encontrado")
            else:
                print(f"Models con {attribute} = {element} encontrado en el objeto: {index}")
        
        self.toList(array)
        return self

#--------------------------Binario Secuencial------------------------------------------------------------------------------------------------
    def search_binarySecuencial(self, element):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            search = BinarySecuencial()
            index = search.search_BinarySecuencial(array, element)
            if index == -1:
                print(f"Elemento {element} no encontrado")
            else:
                print(f"Elemento {element} fue encontrado en estas ocasiones: {index}")
        
        self.toList(array)
        return self

    def search_binarySecuencial_models(self, element, attribute):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            
            array = self.toArray
            search = BinarySecuencial()
            index = search.search_BinarySecuencial_models(array, element, attribute)
            aux = []
            if index == -1:
                print(f"Models con {attribute} = {element} no encontrado")
            else:
               # print(f"{Fore.GREEN}los modelos con {attribute} = {element} fueron encontrados en: ") #{index}
                
                for i in range(0, len(index)):
                    aux.append(index[i])
        self.toList(aux)
        
    #-------------------------- Secuencial------------------------------------------------------------------------------------------------
    

    def __str__(self) -> str:
        out = ""
        if self.isEmpty:
            out = "List is Empty"
        else:
            node = self.__head
            while node != None:
                out += str(node._data)+ "\t"
                node = node._next
        return out

    @property
    def print(self):
        node = self.__head
        data = ""    
        while node != None:
            data += str(node._data)+"    "            
            node = node._next
        print("Lista de datos")
        print(data)
    """ @property
    def print(self):
       node = self.__head
       data = ''

       while node != None:
            data += str(node._data._id)+ '    '
            node = node._next            
            print(data) """