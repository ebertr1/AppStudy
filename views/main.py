import sys
sys.path.append('../')


from controls.asignacionDaoControl import AsignacionDaoControl
from  controls.cuentaDaoControl import CuentaDaoControl
from controls.rolDaoControl import RolDaoControl
from controls.unidadDaoControl import UnidadDaoControl
from controls.cicloDaoControl import CicloDaoControl
from controls.mallaDaoControl import MallaDaoControl
from controls.parametrosDaoControl import ParametrosDaoControl
from controls.docenteDaoControl import DocenteDaoControl
from controls.personaDaoControl import PersonaDaoControl
from controls.estudianteDaoControl import EstudianteDaoControl
from controls.tda.linked.linkedList import Linked_List
from controls.personaDaoControl import PersonaDaoControl
import random

p = PersonaDaoControl()
asig = AsignacionDaoControl()
cu = CuentaDaoControl()
r = RolDaoControl()
u = UnidadDaoControl()
ci = CicloDaoControl()
mll = MallaDaoControl()
param = ParametrosDaoControl()
docnt= DocenteDaoControl()
person = PersonaDaoControl()
est = EstudianteDaoControl()
try:
    """param._parametros._aprendizajeAutonomo = '6'
    param._parametros._evaluacionUnidad = '7'
    param._parametros._aprendizajeDocente = '8'
    param._parametros._aprendizajeExperimental = '9'
    param._parametros._lecciones = '10'
    param.save
    param._parametros = None

    mll._malla._nombre = 'Malla 1'
    mll._malla._descripcion = 'Malla curricular de la carrera de Ingenieria en Sistemas'
    mll._malla._fechaCreacion = '2021-10-10'
    mll.save
    mll._malla = None
    ci._ciclo._numeroCiclo = '1'
    ci._ciclo._paralelo = 'A'
    ci.save
    ci._ciclo = None
    u._unidad._numeroUnidad = '2'
    u._unidad._duracionSemanas = '3 semanas'
    u.save
    u._unidad = None
    r._rol._nombre = 'Estudiante'
    r._rol._descripcion = 'Rol para estudiantes'
    r.save
    r._rol = None
    asig._asignacion._cedulaDocente = '1234567890'
    asig._asignacion._paralelo = 'A'
    asig._asignacion._tipoIdentificacion = 'CEDULA'
    asig.save
    asig._asignacion = None
    cu._cuenta._correoInstitucional = ' sjsjsj@unl.edu.ec'
    cu._cuenta._contrasenia = '12343344 '
    cu.save
    cu._cuenta = None
    listaS = Linked_List()
    listaS.add("A", listaS._length)
    listaS.add("B", listaS._length)
    listaS.add("C", listaS._length)
    listaS.add("D", listaS._length)
    listaS.print
    listaS.sort(1)
    listaS.print
    cu._list().print
    listaAux = cu._list().sort_models("_correoInstitucional", 2)
    listaAux.print"""
    #p._persona._id = 1
    p._persona._apellido = 'GIla'
    p._persona._nombre = 'Juan'
    p._persona._direccion = 'Quito'
    p.save
    p._persona = None

except Exception as e:
    print(e)