import sys
sys.path.append('../')


from controls.asignacionDaoControl import AsignacionDaoControl
from  controls.cuentaDaoControl import CuentaDaoControl
from controls.rolDaoControl import RolDaoControl
from controls.unidadDaoControl import UnidadDaoControl
from controls.cicloDaoControl import CicloDaoControl

asig = AsignacionDaoControl()
cu = CuentaDaoControl()
r = RolDaoControl()
u = UnidadDaoControl()
ci = CicloDaoControl()
try:
    ci._ciclo._numeroCiclo = '1'
    ci._ciclo._paralelo = 'A'
    ci.save
    ci._ciclo = None
    """u._unidad._numeroUnidad = '2'
    u._unidad._duracionSemanas = '3 semanas'
    u.save
    u._unidad = None"""
    """r._rol._nombre = 'Estudiante'
    r._rol._descripcion = 'Rol para estudiantes'
    r.save
    r._rol = None"""
    """asig._asignacion._cedulaDocente = '1234567890'
    asig._asignacion._paralelo = 'A'
    asig._asignacion._tipoIdentificacion = 'CEDULA'
    asig.save
    asig._asignacion = None"""
    """cu._cuenta._correoInstitucional = ' sjsjsj@unl.edu.ec'
    cu._cuenta._contrasenia = '12343344 '
    cu.save
    cu._cuenta = None"""


   

except Exception as e:
    print(e)