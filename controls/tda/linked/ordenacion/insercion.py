class Insercion:

    def sort_primitive_ascendent(self, array): 
        for i in range(1, len(array)):
            j = i - 1
            t = array[i]
            while j >= 0 and t < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = t

        return array

    def sort_primitive_descendent(self, array): 
        for i in range(1, len(array)):
            j = i - 1
            t = array[i]
            while j >= 0 and t > array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = t

        return array
    
    def sort_models_ascendent(self, array, attribute): 
        for i in range(1, len(array)):
            j = i - 1
            t = array[i]
            while j >= 0 and getattr(t , attribute) < getattr(array[j], attribute):
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = t

        return array

    def sort_models_descendent(self, array, attribute): 
        for i in range(1, len(array)):
            j = i - 1
            t = array[i]
            while j >= 0 and getattr(t , attribute) > getattr(array[j], attribute):
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = t
            
        return array

    #getattr(array[j - 1], attribute) > getattr(array[j], attribute):