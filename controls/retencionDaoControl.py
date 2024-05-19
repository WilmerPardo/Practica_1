from controls.dao.daoAdapter import DaoAdapter
from models.retencion import Retencion

class RetencionDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Retencion)  
        self.__retencion = None
        

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
    
    
    def save(self):
        print(self.stack._stack)
        self.__retencion._id = self.stack._length + 1
        self._save(self.__retencion._historialRetenciones)
    

