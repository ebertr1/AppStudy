import pyodbc

# Configuración de la conexión
username = 'user_developer'
password = '123456'
dsn = '64'  # Nombre del DSN configurado en ODBC

# Crear una conexión
try:
    connection = pyodbc.connect('DSN=' + dsn + ';UID=' + username + ';PWD=' + password)

    # Información del servidor Oracle
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM V$VERSION')
    row = cursor.fetchone()
    print("Versión del servidor:", row)

except pyodbc.Error as error:
    print("Error al conectar a Oracle:", error)

finally:
    # Cerrar la conexión al finalizar
    if 'connection' in locals():
        connection.close()
        print("Conexión cerrada.")
