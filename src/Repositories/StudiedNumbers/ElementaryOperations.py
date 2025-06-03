from Repositories.Numbers.Number import Number
from Repositories.Numbers.Binary import Binary
from Repositories.Numbers.Decimal import Decimal
from Repositories.Numbers.Hexadecimal import Hexadecimal
from Repositories.StudiedNumbers.NumeralSystem import NumeralSystem
from Structures.LinkedList import LinkedList

class ElementaryOperations:
    
    def __init__(self, numeralSystems:NumeralSystem):
        self.__operations:LinkedList = LinkedList()
        self.__checkElementaryOperations(numeralSystems.getSystem())
    
    def __checkElementaryOperations(self, numeralSystems:LinkedList):
        classesOfNumeralSystems:dict[str:Number] = {
            "binario" : Binary,
            "decimal" : Decimal,
            "hexadecimal" : Hexadecimal
        }
        list = LinkedList()
        
        for i in range(numeralSystems.getSize()):
            list.addLast(classesOfNumeralSystems[numeralSystems.get(i)].getElementaryOperations())

        elementaryOperations = self.__findCommonStrings(list)
        self.__operations = elementaryOperations
    
    def __findCommonStrings(self, listOfLists:LinkedList) -> LinkedList:
        if not listOfLists:
            raise ValueError("Error: La lista de listas es inválida")
        
        commonItems = LinkedList()
        
        firstList:LinkedList = listOfLists.get(0)
        for i in range(firstList.getSize()):
            if (not commonItems.contains(firstList.get(i))):
                commonItems.addLast(firstList.get(i))
                
        for i in range(1, listOfLists.getSize()):
            currentList:LinkedList = listOfLists.get(i)
            temporalList = LinkedList()
            for i in range(commonItems.getSize()):
                if currentList.contains(commonItems.get(i)):
                    temporalList.addLast(commonItems.get(i))
            commonItems = temporalList
                
        return commonItems
    
    def __str__(self):
        text = ""
        for i in range(self.__operations.getSize()):
            if (i == self.__operations.getSize() - 1):
                text += f"{self.__operations.get(i)}"
            else: 
                text += f"{self.__operations.get(i)}, "
        return text

    def __validateValue(self, value:str) -> None:
        if (value.__class__.__name__ == "str"):
            validChars = ".0123456789abcdefABCDEF"
            numberOfPoints = 0
            for char in value:
                if (char not in validChars):
                    raise ValueError("Error: El valor ingresado posee caracteres no válidos")
                elif (char == "." and numberOfPoints == 1):
                    raise ValueError("Error: El formato del número con punto decimal es incorrecto")
                elif (char == "."): 
                    numberOfPoints += 1
        else:
            raise ValueError("Error: El valor ingresado debe ser un string")

