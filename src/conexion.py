import cx_Oracle
try:
    connection= cx_Oracle.connect(
      user='PIS',
      password='unl123',
      dsn='localhost:1521/XE',
      encoding='UTF-8'
      
    )
    print(connection.version)
except Exception as ex:
    print(ex)

cur_01 = connection.cursor()
crea_tabla = '''create table prueba(
campo1 varchar2(40),
campo2 int not null)'''
cur_01.execute(crea_tabla)
connection.close()