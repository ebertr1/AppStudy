class Sacudida:
    #crear el metodo def sort_primitive_ascendent utilizando el algorithms de shakesort que utiliza un do while
    def sort_primitive_ascendent(self, array):
        len_array = len(array)
        left = 0
        right = len_array - 1
        while left < right:
            for i in range(left, right):
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
            right -= 1
            for i in range(right, left, -1):
                if array[i - 1] > array[i]:
                    array[i - 1], array[i] = array[i], array[i - 1]
            left += 1
        return array
    
    def sort_primitive_descendent(self, array):
        len_array = len(array)
        left = 0
        right = len_array - 1
        while left < right:
            for i in range(left, right):
                if array[i] < array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
            right -= 1
            for i in range(right, left, -1):
                if array[i - 1] < array[i]:
                    array[i - 1], array[i] = array[i], array[i - 1]
            left += 1
        return array
    
    def sort_models_ascendent(self, array, attribute):
        len_array = len(array)
        left = 0
        right = len_array - 1
        while left < right:
            for i in range(left, right):
                if getattr(array[i], attribute) > getattr(array[i + 1], attribute):
                    array[i], array[i + 1] = array[i + 1], array[i]
            right -= 1
            for i in range(right, left, -1):
                if getattr(array[i - 1], attribute) > getattr(array[i], attribute):
                    array[i - 1], array[i] = array[i], array[i - 1]
            left += 1
        return array

    def sort_models_descendent(self, array, attribute):
        len_array = len(array)
        left = 0
        right = len_array - 1
        while left < right:
            for i in range(left, right):
                if getattr(array[i], attribute) < getattr(array[i + 1], attribute):
                    array[i], array[i + 1] = array[i + 1], array[i]
            right -= 1
            for i in range(right, left, -1):
                if getattr(array[i - 1], attribute) < getattr(array[i], attribute):
                    array[i - 1], array[i] = array[i], array[i - 1]
            left += 1
        return array