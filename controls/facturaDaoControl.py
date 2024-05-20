from models.factura import Factura
from controls.dao.daoAdapterLinked import DaoAdapterLinked

class FacturaDaoControl(DaoAdapterLinked):
    def __init__(self):
        super().__init__(Factura)
        self.__factura = None
        self.__tipo_ruc = Factura._tipo_ruc

    @property
    def _tipo_ruc(self):
        return self.__tipo_ruc

    @_tipo_ruc.setter
    def _tipo_ruc(self, value):
        self.__tipo_ruc = value

    @property
    def _factura(self):
        if self.__factura is None:
            self.__factura = Factura()
        return self.__factura

    @_factura.setter
    def _factura(self, value):
        self.__factura = value


    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self.__factura._id = self._lista._length + 1
        self._save(self.__factura)

    @property
    def get_all(self):
       # for factura in self.lista.get_all_invoices:
        #    return(factura)
        return self.lista.get_all_invoices
    
    @property
    def serializer(self):
        return self.__factura.serializer