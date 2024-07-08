class Cursa:
    def __init__(self):
        self.__id = 0

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def serializable(self):
        return {
            "id": self._id
        }
    def deserializar(self, data):
        cursa = Cursa()
        cursa._id = data['id']
        return cursa
    
