import numpy as np
from Repositories.Numbers.Number import Number
from Structures.LinkedList import LinkedList

class Hexadecimal(Number):
    _digits = np.array(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"])
    _base = len(_digits)
    def __init__(self, value:str):
        self._value = ""
        self._validateAndSetValue(value)
    
    @property
    def value(self):
        return self._value
    
    @property
    def digits(self):
        return self._digits
    
    @property
    def base(self):
        return self._base
    
    @staticmethod
    def getElementaryOperations() -> LinkedList:
        list = LinkedList()
        number1 = Hexadecimal("101")
        number2 = Hexadecimal("111")

        try:
            number1 + number2
            list.addLast("+")
        except TypeError as error:
            pass
        try:
            number1 - number2
            list.addLast("-")
        except TypeError as error:
            pass
        try:
            number1 * number2
            list.addLast("*")
        except TypeError as error:
            pass
        try:
            number1 / number2
            list.addLast("/")
        except TypeError as error:
            pass
        
        return list