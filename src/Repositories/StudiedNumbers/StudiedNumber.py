from Process.ErrorHandling.Exceptions import *
from Repositories.StudiedNumbers.SignificantFigures import SignificantFigures
from Repositories.StudiedNumbers.NumeralSystem import NumeralSystem
from Repositories.StudiedNumbers.Bases import Bases
from Repositories.StudiedNumbers.ElementaryOperations import ElementaryOperations

class StudiedNumber:
    def __init__(self, value:str):
        self.__validateAndSetValue(value)
        self.__significantFigures:SignificantFigures = SignificantFigures(value)
        self.__numeralSystem:NumeralSystem = NumeralSystem(value)
        self.__bases:Bases = Bases(self.__numeralSystem)
        self.__elementaryOperations:ElementaryOperations = ElementaryOperations(self.__numeralSystem)

    def __validateAndSetValue(self, value:str) -> None:
        if value is None:
            raise NoneType("Error: Has ingresado un valor nulo")

        if not isinstance(value, str):
            raise ValueError("Error: El valor ingresado debe ser un string")
        
        validChars = ".0123456789abcdefABCDEF"
        
        for char in value:
            if char not in validChars:
                raise NumberIsInvalid("Error: El valor ingresado posee caracteres inválidos")
        
            if value.count(".") > 1:
                raise NumberIsInvalid("Error: El formato del número con punto decimal es incorrecto")

            
            self.__value = value

    def __str__(self) -> str:
        return f"""
Valor: {self.__value}
Cifras significativas: {self.__significantFigures}
Sistemas numéricos posibles: {self.__numeralSystem}
Bases posibles: {self.__bases}
Operaciones elementales que se pueden realizar en este sistema: {self.__elementaryOperations}
        """