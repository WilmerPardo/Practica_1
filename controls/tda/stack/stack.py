from controls.tda.stack.stackOperation import StackOperation

class Stack ():
    def __init__(self, tope):
        self.__stack = StackOperation(tope)
        self.__length = 0

    @property
    def _length(self):
        return self.__length

    @_length.setter
    def _length(self, value):
        self.__length = value

    @property
    def _stack(self):
        return self.__stack

    @_stack.setter
    def _stack(self, value):
        self.__stack = value

        self._length = 0


    def push(self, data):
        self.__stack.push(data)
        self._length += 1
    
    @property
    def pop(self):
        self._length -= 1
        return self.__stack.pop
    
    

    @property
    def verifyTope(self):
        return self.__stack.verifyTope
    
    @property
    def print(self):
        self.__stack.print
   

    def is_empty(self):
        return self.__stack.is_empty
    
    @property
    def clear(self):
        self.__stack.clear

        