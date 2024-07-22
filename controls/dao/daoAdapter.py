from typing import TypeVar, Generic, List
from controls.tda.linked.linkedList import Linked_List
from controls.connection.connection import Connection
import oracledb

T = TypeVar('T')

class DaoAdapter(Generic[T]):
    atype: T
    
    def __init__(self, atype: T):
        self.atype = atype
        self.lista = Linked_List()
        self.connection = Connection().connect()
    
    def _list(self) -> List[T]:
        cursor = self.connection._db.cursor()
        query = f"SELECT * FROM {self.atype.__name__.lower()}"
        cursor.execute(query)
        rows = cursor.fetchall()
        self.lista.clear()
        for row in rows:
            data_dict = {description[0]: value for description, value in zip(cursor.description, row)}
            obj = self.atype().deserializar(data_dict)
            self.lista.add(obj, self.lista._length)
        cursor.close()
        return self.lista
    
    def to_dic(self) -> List[dict]:
        aux = []
        self._list()
        for i in range(self.lista._length):
            aux.append(self.lista.get(i).serializable)
        return aux
    
    def _save(self, data: T):
        cursor = self.connection._db.cursor()
        columns = ', '.join(k for k in data.serializable.keys() if k != 'id')
        values = ', '.join([f":{k}" for k in data.serializable.keys() if k != 'id'])
        query = f"INSERT INTO {self.atype.__name__.lower()} ({columns}) VALUES ({values})"
        cursor.execute(query, {k: v for k, v in data.serializable.items() if k != 'id'})
        self.connection._db.commit()
        cursor.close()

        
    def _merge(self, data: T, pos):
        cursor = self.connection._db.cursor()
        set_clause = ', '.join([f"{k} = :{k}" for k in data.serializable.keys() if k != 'id'])
        query = f"UPDATE {self.atype.__name__.lower()} SET {set_clause} WHERE id = :id"
        cursor.execute(query, {**{k: v for k, v in data.serializable.items() if k != 'id'}, 'id': pos})
        self.connection._db.commit()
        cursor.close()
