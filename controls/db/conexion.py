
import oracledb

class Conexion():
    def __init__(self):
        self.__db = None 

    @property
    def _db(self):
        return self.__db

    @_db.setter
    def _db(self, value):
        self.__db = value
  
    def connection(self, user= 'user_developer', password='123456', dsn='localhost:1521/xe'):
       try:
           self.__db = oracledb.connect(user, password, dsn)
           print('Conexion exitosa')
           return self.__db
       except Exception as e:
            print(e)
            return None
    def close(self):
        self.__db.close()