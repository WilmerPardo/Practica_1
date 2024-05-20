from typing import TypeVar, Generic, List
from controls.tda.stack.stack import Stack
import os.path
import json
import os

T = TypeVar('T')
class DaoAdapter(Generic[T]):
    atype: T
    def __init__(self, atype: T):
        self.atype = atype
        self.file = atype.__name__.lower() + ".json"
        self.stack = Stack(10)
        self.URL = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+"/data/"

    def _list(self) -> T:
        if os.path.isfile(self.URL+self.file):
            f = open(self.URL+self.file, "r")
            datos = json.load(f)
            self.stack.clear
            for data in datos:
#                print(type(data))
                a = self.atype().deserializer(data)
                self.stack.push(a)
            f.close()
        return self.stack
    
    

    def __transform__(self):
        aux = ""
        for i in range(self.stack._stack._length):
            aux += self.stack._stack.get(i)._stack.serializer
            if i < self.stack._stack._length - 1:
                aux += ","
        aux += ""
        return aux

    def to_dic(self):
        aux = []
        temp_stack = Stack(10)
        while not self.stack.is_empty():
            data = self.stack.pop  
            aux.append(data.serializer)
            temp_stack.push(data)
        while not temp_stack.is_empty():
            self.stack.push(temp_stack.pop)
        return aux
    

    def _save(self, data: T):
        self._list()
        self.stack.push(data)
        f = open(self.URL+self.file, "w")
        f.write(self.__transform__())
        f.close()

        
    
    def merge(self, data: T):
        _ = self.stack.pop
        self.stack.push(data)
        with open(self.URL + self.file, "w") as a:
            a.write(self.__transform__())