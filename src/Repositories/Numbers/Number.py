from __future__ import annotations
import numpy as np
from abc import ABC, abstractmethod
from Structures.LinkedList import LinkedList

class Number(ABC):
    def __init__(self):
        pass

    @property
    @abstractmethod
    def value(self):
        pass
    
    @property
    @abstractmethod
    def digits(self):
        pass
    
    @property
    @abstractmethod
    def base(self):
        pass
    
    def getValue(self) -> str:
        return self._value
    
    def __add__(self, anotherNumber:Number) -> Number:
        if (isinstance(anotherNumber, self.__class__)):
            maxLength:int = self.__getMaxLength(self._value, anotherNumber.getValue())
            
            digitsOfNumber1:np.ndarray = self.__getValuesOf(self._value, maxLength)
            digitsOfNumber2:np.ndarray = self.__getValuesOf(anotherNumber._value, maxLength)

            carry:int = 0
            resultDigits:LinkedList = LinkedList()
            
            for i in range(maxLength -1, -1, -1):
                totalSum:int = digitsOfNumber1[i] + digitsOfNumber2[i] + carry
                actualDigit:int = totalSum % self._base
                carry:int = totalSum // self._base

                resultDigits.addFirst(actualDigit)
                
            if (carry > 0):
                resultDigits.addFirst(carry)
                
            resultString:str = self.__convertToString(resultDigits)
            
            return self.__class__((resultString))
        else:
            raise TypeError("Error: No se puede sumar números de distintos sistemas numéricos")

    def __sub__(self, anotherNumber:Number) -> Number:
        if (isinstance(anotherNumber, self.__class__)):
            maxLength:int = self.__getMaxLength(self._value, anotherNumber.getValue())
            
            digitsOfNumber1:np.ndarray = self.__getValuesOf(self._value, maxLength)
            digitsOfNumber2:np.ndarray = self.__getValuesOf(anotherNumber._value, maxLength)
            
            borrow:int = 0
            resultDigitsInt:LinkedList = LinkedList()

            for i in range(maxLength -1, -1, -1):
                digit1:int = digitsOfNumber1[i]
                digit2:int = digitsOfNumber2[i]

                currentDigit1:int = digit1 - borrow
                
                if currentDigit1 < digit2:
                    currentDigit1 += self._base
                    borrow = 1
                else:
                    borrow = 0
                    
                actualSubstraction:int = currentDigit1 - digit2
                resultDigitsInt.addFirst(actualSubstraction)
            
            resultString:str = self.__convertToString(resultDigitsInt)
            return self.__class__((resultString))
        else:
            raise TypeError("Error: No se puede sumar números de distintos sistemas numéricos")

    def __mul__(self, anotherNumber:Number) -> Number:
        if isinstance(anotherNumber, self.__class__):
            digitsOfNumber1:np.ndarray = self.__getValuesOf(self._value, len(self._value))
            digitsOfNumber2:np.ndarray = self.__getValuesOf(anotherNumber.getValue(), len(anotherNumber.getValue()))
            
            maxLengthOfResult:int = len(self._value) + len(anotherNumber.getValue())
            intermediateAdittions:np.ndarray = np.full(maxLengthOfResult, 0, dtype=int)
            

            for i in range(len(digitsOfNumber2) - 1, -1, -1):
                digit2:int = digitsOfNumber2[i]
                carry:int = 0
                for j in range(len(digitsOfNumber1) - 1, -1, -1):
                    digit1:int = digitsOfNumber1[j]
                    
                    product:int = digit1 * digit2 + carry
                    
                    position1FromRight:int = len(digitsOfNumber1) - 1 - j
                    position2FromRight:int = len(digitsOfNumber2) - 1 - i
                    
                    combinedPositionFromRight:int = position1FromRight + position2FromRight
                    
                    position:int = (maxLengthOfResult - 1) - combinedPositionFromRight
                    
                    total:int = intermediateAdittions[position] + (product % self._base)
                    intermediateAdittions[position] = total % self._base
                    
                    carry = (product // self._base) + (total // self._base)
                
                remainingCarryPosition:int = (maxLengthOfResult - 1) - ((len(digitsOfNumber2) - 1 - i) + len(digitsOfNumber1))
                while carry > 0:
                    intermediateAdittions[remainingCarryPosition] += carry % self._base
                    carry = carry // self._base
                    remainingCarryPosition -= 1

            finalResultDigits:np.ndarray = np.full(maxLengthOfResult, 0, dtype=int)
            carry = 0
            for k in range(maxLengthOfResult - 1, -1, -1):
                total = intermediateAdittions[k] + carry
                finalResultDigits[k] = total % self._base
                carry = total // self._base
            
            finalDigitsList:LinkedList = self.__convertNdarrayToLinkedList(finalResultDigits)
            while carry > 0:
                finalDigitsList.addFirst(carry % self._base)
                carry = carry // self._base

            resultString = self.__convertToString(finalDigitsList)        
            return self.__class__((resultString))
        else:
            raise TypeError("Error: No se pueden multiplicar números de distintos sistemas numéricos")
    
    def __getValuesOf(self, value:str, lenght:int) -> np.ndarray[int]:
        listOfValues:np.ndarray = np.full(lenght, 0, dtype=int)
        
        i = -1
        for charIndex in range(len(value) - 1, -1, -1):
            char:str = value[i]
            listOfValues[i] = self.__getIndexOf(char)
            i -= 1
        return listOfValues

    def __getIndexOf(self, digit:str) -> int:
        if (digit in self._digits):
            for i in range(len(self._digits)):
                if (digit == self._digits[i]):
                    return i
        else:
            raise ValueError("Error: El valor que has ingresado no pertenece al sistema numérico")
        
    def __getMaxLength(self, digitsOfNumber1:str, digitsOfNumber2:str) -> int:
        if (len(digitsOfNumber1) > len(digitsOfNumber2)):
            return len(digitsOfNumber1)
        else:
            return len(digitsOfNumber2)
        
    
    def __convertToString(self, valueList:LinkedList) -> str:
        tempValueChars:LinkedList = LinkedList()
        isLeadingZero:bool = True

        for i in range(valueList.getSize()):
            digitInt:int = valueList.get(i)
            
            if digitInt != 0:
                isLeadingZero = False
            
            if not isLeadingZero:
                if digitInt >= len(self._digits):
                    raise ValueError("Error: El valor calculado excede la base")
                tempValueChars.addLast(self._digits[digitInt])
        
        if not tempValueChars:
            return "0"
        
        finalValue:str = ""
        for i in range(tempValueChars.getSize()):
            finalValue += tempValueChars.get(i)
        
        return finalValue
    
    def __convertNdarrayToLinkedList(self, array:np.ndarray) -> LinkedList:
        newList = LinkedList()
        for i in range(len(array)):
            newList.addLast(array[i])
        return newList
    
    def _validateAndSetValue(self, value:str) -> None:
        if (isinstance(value, str)):
            value = value.upper()
            numberOfDecimalPoints:int = 0
            for char in value:
                if (char == "." and numberOfDecimalPoints == 0):
                    numberOfDecimalPoints += 1
                elif (char == "." and numberOfDecimalPoints > 0):
                    raise ValueError("Error: El valor ingresado posee un formato inválido")
                if (char not in self._digits):
                    raise ValueError("Error: El valor ingresado posee digitos no soportados por el sistema numérico")
            self._value = value
        else:
            raise ValueError("Error: El valor debe ser expresado en un String")
    
    def __str__(self):
        return f"{self._value} (base {self._base})"
