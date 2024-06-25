class QuickSort:
    def sort_primitive_ascendent(self, array):
        if len(array) <= 1:
            return array
        else:
            pivot = array.pop() # Selecciona el último elemento como pivote
        items_greater = []
        items_lower = []
        for item in array:
            if item > pivot:
                items_greater.append(item)
            else:
                items_lower.append(item)
        return self.sort_primitive_ascendent(items_lower) + [pivot] + self.sort_primitive_ascendent(items_greater)

    def sort_primitive_descendent(self, array):
        if len(array) <= 1:
            return array
        else:
            pivot = array.pop()
        items_greater = []
        items_lower = []
        for item in array:
            if item < pivot:
                items_greater.append(item)
            else:
                items_lower.append(item)
        return self.sort_primitive_descendent(items_lower) + [pivot] + self.sort_primitive_descendent(items_greater)
    
    def sort_models_ascendent(self, array, attribute):
        if len(array) <= 1:
            return array
        else:
            pivot = array.pop()
        items_greater = []
        items_lower = []
        for item in array:
            if getattr(item, attribute) > getattr(pivot, attribute):
                items_greater.append(item)
            else:
                items_lower.append(item)
        return self.sort_models_ascendent(items_lower, attribute) + [pivot] + self.sort_models_ascendent(items_greater, attribute)
    
    def sort_models_descendent(self, array, attribute):
        if len(array) <= 1:
            return array
        else:
            pivot = array.pop()
        items_greater = []
        items_lower = []
        for item in array:
            if getattr(item, attribute) < getattr(pivot, attribute):
                items_greater.append(item)
            else:
                items_lower.append(item)
        return self.sort_models_descendent(items_lower, attribute) + [pivot] + self.sort_models_descendent(items_greater, attribute)