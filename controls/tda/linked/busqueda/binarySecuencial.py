
from controls.tda.linked.busqueda.binary import Binary
from controls.tda.linked.busqueda.secuencial import Secuencial
from controls.tda.linked.ordenacion.quickSort import QuickSort

class BinarySecuencial:

    def search_BinarySecuencial(self, array, element):
        quickSort = QuickSort()
        binary = Binary()
        secuencial = Secuencial()

        sorted_array = quickSort.sort_primitive_ascendent(array)
        index = binary.search_binary(sorted_array, element)
        if index == -1:
            return -1
        
        return secuencial.search_sequential(sorted_array, element, index)
    
    def search_BinarySecuencial_models(self, array, element, attribute):
        quickSort = QuickSort()
        binary = Binary()
        secuencial = Secuencial()
        sorted_array = quickSort.sort_models_ascendent(array, attribute)

        index = binary.search_binary_models(sorted_array, element, attribute)
        if index == -1:
            return -1
        #print(secuencial.search_sequential_models(sorted_array, element, attribute, index))
        return secuencial.search_sequential_models(sorted_array, element, attribute, index)
