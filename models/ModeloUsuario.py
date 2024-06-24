class ModeloUsuario():
    def login(self, db, user):
        try:
            cursor=db.connection.cursor()
        except Exception as ex:
            raise Exception(ex)