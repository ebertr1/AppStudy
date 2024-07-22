import oracledb

class Connection:
    def __init__(self):
        self.__db = None 

    @property
    def _db(self):
        return self.__db

    @_db.setter
    def _db(self, value):
        self.__db = value

    def connect(self):
        try:
            self.__db = oracledb.connect(
                user='user_pis',
                password='eber2005',
                dsn='localhost:1521/xe'
            )
        except Exception as error:
            print('Error de conexión: ', error)
            exit()
        else:
            print('Conexión exitosa', self.__db.version)
        return self

    def close(self):
        if self.__db:
            self.__db.close()

