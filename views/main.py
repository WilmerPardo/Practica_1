import sys
sys.path.append('../')

#from models.factura import Factura
#from models.retencion import Retencion
from controls.retencionDaoControl import RetencionDaoControl
from controls.facturaDaoControl import FacturaDaoControl



facturaDao = FacturaDaoControl()
#retencion = Retencion()
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
        historial.generarRetencion(factura)
    #historial.generarRetencion(facturaDao.get_all)
    historial.printHistorial()

    #historial.generarRetencion(facturaDao.lista.get_all_invoices)

    historial.save()

except Exception as e:
    print(e)