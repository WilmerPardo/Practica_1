from controls.dao.daoAdapter import DaoAdapter
from controls.tda.stack.stack import Stack
from models.retencion import Retencion
from models.factura import Factura

class RetencionDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Retencion)  
        self.__retencion = None
        self.__historial = Stack(20)

    @property
    def _historial(self):
        return self.__historial

    @_historial.setter
    def _historial(self, value):
        self.__historial = value
 
    @property
    def _stack(self):
        return self.__stack

    @_stack.setter
    def _stack(self, value):
        self.__stack = value

    @property
    def _retencion(self):
        if self.__retencion is None:
            self.__retencion = Retencion()
        return self.__retencion

    @_retencion.setter
    def _retencion(self, value):
        self.__retencion = value

    @property
    def _lista(self):
        return self._list()
    
    def calcularRetencion(self, factura: Factura) -> float:
        retencion = 0.0
        if factura._tipo_ruc == "EDUCATIVO":
            retencion = factura._monto * 0.08
        elif factura._tipo_ruc == "PROFESIONAL":
            retencion = factura._monto * 0.1
        return round(retencion, 2)
    
    def generarRetencion(self, factura: Factura):
        retencion = self.calcularRetencion(factura)
        self.__historial.push({"factura": factura.serializer, "retencion": retencion})
        return self
    
    def printHistorial(self):
        print('Historial de retenciones:')
        self.__historial.print
        print('')
        


    def save(self):
        if self.__retencion is None:
            self.__retencion = Retencion()
        self.__retencion._id = self.stack._length + 1
        self._save(self.__historial)

       