from models.factura import Factura
from controls.tda.stack.stack import Stack

class Retencion:
    def __init__(self):
        self.__id = 0 
        self.__historialRetenciones = ''

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _historialRetenciones(self):
        return self.__historialRetenciones

    @_historialRetenciones.setter
    def _historialRetenciones(self, value):
        self.__historialRetenciones = value

    def calcularRetencion(self, factura: Factura) -> float:
        retencion = 0.0
        if factura._tipo_ruc == "EDUCATIVO":
            retencion = factura._monto * 0.08
        elif factura._tipo_ruc == "PROFESIONAL":
            retencion = factura._monto * 0.1
        return round(retencion, 2)
    
    def generarRetencion(self, factura: Factura):
        retencion = self.calcularRetencion(factura)
        self.__historialRetenciones.push({"factura": factura.serializer, "retencion": retencion})
        return factura
       
    @property
    def printHistorial(self):
        print('Historial de retenciones:')
        self.__historialRetenciones.print
        print('')


    @property
    def serializer(self):
        return {
            'id': self._id,
            'historialRetenciones': self._historialRetenciones.serializer
        }
    
    def deserializer(self, data):
        retencion = Retencion()
        retencion._id = data['id']
        retencion._historialRetenciones = data['historialRetenciones']
        return retencion
    
    