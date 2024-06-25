
class Burbuja:

    def sort_burbuja_number_ascendent(self, array): 
        for i in range(0, (len(array)-1)):
            for j in range(1, len(array)):
                    if array[j - 1] > array[j]:
                        temp = array[j-1]
                        array[j-1] = array[j]
                        array[j] = temp    
        return array

    
    def sort_burbuja_number_descendent(self, array):
        for i in range(0, (len(array)-1)):
            for j in range(1, len(array)):
                if array[j - 1] < array[j]:
                    temp = array[j-1]
                    array[j-1] = array[j]
                    array[j] = temp
        return array
    
    def sort_burbuja_attribute_ascendent(self, array, attribute): 
        for i in range(0, (len(array)-1)):
            for j in range(1, len(array)):
                    #cls = getattr(array[0], "_apellidos")
                    if getattr(array[j - 1], attribute) > getattr(array[j], attribute):
                        temp = array[j-1]
                        array[j-1] = array[j]
                        array[j] = temp    
        return array
    
    def sort_burbuja_attribute_descendent(self, array, attribute): 
        for i in range(0, (len(array)-1)):
            for j in range(1, len(array)):
                    #cls = getattr(array[0], "_apellidos")
                    if getattr(array[j - 1], attribute) < getattr(array[j], attribute):
                        temp = array[j-1]
                        array[j-1] = array[j]
                        array[j] = temp    
        return array
    
    #crear un metodo sort_burbuja para ordenar por fecha 
   