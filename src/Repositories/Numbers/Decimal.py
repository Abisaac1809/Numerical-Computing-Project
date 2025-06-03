from __future__ import annotations
import numpy as np
from Repositories.Numbers.Number import Number
from Structures.LinkedList import LinkedList

class Decimal(Number):
    _digits = np.array(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
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
    
    def __truediv__(self, anotherValue:Decimal):
        return Decimal(str(int(self._value) // int(anotherValue.value)))
    
    @staticmethod
    def getElementaryOperations() -> LinkedList:
        list = LinkedList()
        number1 = Decimal("101")
        number2 = Decimal("111")
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