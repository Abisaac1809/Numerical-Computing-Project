from Repositories.StudiedNumbers.SignificantFigures import SignificantFigures
from Repositories.StudiedNumbers.NumeralSystem import NumeralSystem
from Repositories.StudiedNumbers.Bases import Bases
from Repositories.StudiedNumbers.ElementaryOperations import ElementaryOperations

class StudiedNumber:
    __value = ""

    def __init__(self, value:str):
        self.__validateAndSetValue(value)
        self.__significantFigures:SignificantFigures = SignificantFigures(value)
        self.__numeralSystem:NumeralSystem = NumeralSystem(value)
        self.__bases:Bases = Bases(self.__numeralSystem)
        self.__elementaryOperations:ElementaryOperations = ElementaryOperations(self.__numeralSystem)

    def __validateAndSetValue(self, value:str) -> None:
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
            self.__value = value
        else:
            raise ValueError("Error: El valor ingresado debe ser un string")

    def __str__(self) -> str:
        return f"""
Valor: {self.__value}
Cifras significativas: {self.__significantFigures}
Sistemas numéricos posibles: {self.__numeralSystem}
Bases posibles: {self.__bases}
Operaciones elementales que se pueden realizar en este sistema: {self.__elementaryOperations}
        """

