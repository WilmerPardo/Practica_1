from models.enumTipoRuc import enumTipoRuc

class Factura():
    def __init__(self):
        self.__id = 0
        self.__usuario = ''
        self.__ruc = ''
        self.__monto = 0.00
        self.__tipo_ruc = enumTipoRuc

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _usuario(self):
        return self.__usuario

    @_usuario.setter
    def _usuario(self, value):
        self.__usuario = value

    @property
    def _ruc(self):
        return self.__ruc

    @_ruc.setter
    def _ruc(self, value):
        self.__ruc = value

    @property
    def _monto(self):
        return self.__monto

    @_monto.setter
    def _monto(self, value):
        self.__monto = value

    @property
    def _tipo_ruc(self):
        return self.__tipo_ruc

    @_tipo_ruc.setter
    def _tipo_ruc(self, value):
        self.__tipo_ruc = value

    @property
    def serializer(self):
        return {
            'id': self._id,
            'usuario': self._usuario,
            'ruc': self._ruc,
            'monto': self._monto,
            'tipo_ruc': self._tipo_ruc.__str__()
        }

    def deserializer(self, data):
        self._id = data['id']
        self._usuario = data['usuario']
        self._ruc = data['ruc']
        self._monto = data['monto']
        self._tipo_ruc = data['tipo_ruc']
        return self