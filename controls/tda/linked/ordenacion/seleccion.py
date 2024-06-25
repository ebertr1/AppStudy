class Seleccion:
    def sort_primitive_ascendent(self, array):
        len_array = len(array)
        for i in range(len_array - 1):
            min_index = i
            for j in range(i + 1, len_array):
                if array[j] < array[min_index]:
                    min_index = j
            array[i], array[min_index] = array[min_index], array[i]  
        return array

    def sort_primitive_descendent(self, array):
        len_array = len(array)
        for i in range(len_array - 1):
            max_index = i
            for j in range(i + 1, len_array):
                if array[j] > array[max_index]:
                    max_index = j
            array[i], array[max_index] = array[max_index], array[i]  
        return array

    def sort_models_ascendent(self, array, attribute):
        len_array = len(array)
        for i in range(len_array - 1):
            min_index = i
            for j in range(i + 1, len_array):
                if getattr(array[j], attribute) < getattr(array[min_index], attribute):
                    min_index = j
            array[i], array[min_index] = array[min_index], array[i]  
        return array

    def sort_models_descendent(self, array, attribute):
        len_array = len(array)
        for i in range(len_array - 1):
            max_index = i
            for j in range(i + 1, len_array):
                if getattr(array[j], attribute) > getattr(array[max_index], attribute):
                    max_index = j
            array[i], array[max_index] = array[max_index], array[i] 
        return array