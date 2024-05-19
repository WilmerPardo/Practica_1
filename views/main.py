import sys
sys.path.append('../')

#from models.factura import Factura
from models.retencion import Retencion
from controls.retencionDaoControl import RetencionDaoControl
from controls.facturaDaoControl import FacturaDaoControl

#factura = Factura()
#f1 = Factura()
#f2 = Factura()

facturaDao = FacturaDaoControl()
retencion = Retencion()
historial = RetencionDaoControl()


try:
    facturaDao._factura._monto = 1000.0
    facturaDao._factura._usuario = "Santiago"
    facturaDao._factura._ruc = "1234567890"
    facturaDao._factura._tipo_ruc = "PROFESIONAL"
    facturaDao._factura._fecha = "2021-10-10"
    facturaDao.save

    facturaDao._factura._monto = 2000.0
    facturaDao._factura._usuario = "Andres"
    facturaDao._factura._ruc = "1234567890"
    facturaDao._factura._tipo_ruc = "PROFESIONAL"
    facturaDao._factura._fecha = "2021-10-10"
    facturaDao.save

    facturaDao._factura._monto = 3000.0
    facturaDao._factura._usuario = "Anthony"
    facturaDao._factura._ruc = "1234567890"
    facturaDao._factura._tipo_ruc = "PROFESIONAL"
    facturaDao._factura._fecha = "2021-10-10"
    facturaDao.save

    facturaDao._factura._monto = 1000.0
    facturaDao._factura._usuario = "Cristhian"
    facturaDao._factura._ruc = "1234567890"
    facturaDao._factura._tipo_ruc = "EDUCATIVO"
    facturaDao._factura._fecha = "2021-10-10"
    facturaDao.save


    for factura in facturaDao.get_all:
        retencion.generarRetencion(factura)
        
        historial._retencion.generarRetencion(factura)
        
    retencion.printHistorial

    historial.save()
    
    #factura._usuario = "Santiago"
    #factura._ruc = "1234567890"
    #factura._tipo_ruc = "EDUCATIVO"
    #factura._monto = 1000.0
    #factura._fecha = "2021-10-10"

    #f1._usuario = "Robles"
    #f1._ruc = "1234567890"
    #f1._tipo_ruc = "PROFESIONAL"
    #f1._monto = 1000.0
    #f1._fecha = "2021-10-10"

    #f2._usuario = "Andres"
    #f2._ruc = "1234567890"
    #f2._tipo_ruc = "EDUCATIVO"
    #f2._monto = 1000.0
    #f2._fecha = "2021-10-10"


   # retencion.generarRetencion(factura)
   # retencion.generarRetencion(f1)
   # retencion.generarRetencion(f2)

    #retencion.printHistorial()
except Exception as e:
    print(e)