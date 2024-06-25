
class ShellSort:
    def sort_primitive_ascendent(self, array):
        len_array = len(array)
        gap = len_array // 2
        while gap > 0:
            for i in range(gap, len_array):
                temp = array[i]
                j = i
                while j >= gap and array[j - gap] > temp:
                    array[j] = array[j - gap]
                    j -= gap
                array[j] = temp
            gap //= 2
        
        return array
    
    def sort_primitive_descendent(self, array):
        len_array = len(array)
        gap = len_array // 2
        while gap > 0:
            for i in range(gap, len_array):
                temp = array[i]
                j = i
                while j >= gap and array[j - gap] < temp:
                    array[j] = array[j - gap]
                    j -= gap
                array[j] = temp
            gap //= 2
        return array
    
    def sort_models_ascendent(self, array, attribute):
        len_array = len(array)
        gap = len_array // 2
        while gap > 0:
            for i in range(gap, len_array):
                temp = array[i]
                j = i
                while j >= gap and getattr(array[j - gap], attribute) > getattr(temp, attribute):
                    array[j] = array[j - gap]
                    j -= gap
                array[j] = temp
            gap //= 2
        return array
    
    def sort_models_descendent(self, array, attribute):
        len_array = len(array)
        gap = len_array // 2
        while gap > 0:
            for i in range(gap, len_array):
                temp = array[i]
                j = i
                while j >= gap and getattr(array[j - gap], attribute) < getattr(temp, attribute):
                    array[j] = array[j - gap]
                    j -= gap
                array[j] = temp
            gap //= 2
        return array