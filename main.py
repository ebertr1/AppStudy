# import sys

# sys.path.append('../')
# from controls.db.conexion import Conexion
# Sn = Conexion()
# Sn.connection()
import sys
sys.path.append('../')
from controls.personaDaoControl import PersonaDaoControl

p = PersonaDaoControl()
try:
    p._persona._nombre = 'Isabel'
    p._persona._apellido = 'Morocho'
    p._persona._dirección= 'Calle 1'
    p.save
    p._persona = None
    
except Exception as e:
    print(e)