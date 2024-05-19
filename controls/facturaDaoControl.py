from models.factura import Factura
from controls.dao.daoAdapterLinked import DaoAdapterLinked

class FacturaDaoControl(DaoAdapterLinked):
    def __init__(self):
        super().__init__(Factura)
        self.__factura = None

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
        return self.lista.get_all_invoices
    