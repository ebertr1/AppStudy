import sys

sys.path.append('../')
from controls.db.conexion import Conexion
Sn = Conexion()
Sn.connection()
