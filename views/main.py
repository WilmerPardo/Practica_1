import sys
sys.path.append('../')
import os
import psutil
from time import time

from controls.retencionDaoControl import RetencionDaoControl
from controls.facturaDaoControl import FacturaDaoControl


facturaDao = FacturaDaoControl()
#retencion = Retencion()
historial = RetencionDaoControl()


try:
    # tiempoInicio = time() 

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
        historial.generarRetencion(factura) #ESTO UTILIZA PILAS
   
    historial.printHistorial()
    historial.save()


    """ 
    tiempoFinal = time()
    print("Tiempo de ejecución: ", tiempoFinal - tiempoInicio)

    process = psutil.Process(os.getpid())
    memory_usage = process.memory_info().rss / 1024 ** 2
    print(f"La memoria utilizada por el programa es: {memory_usage} MB") """

except Exception as e:
    print(e)


    