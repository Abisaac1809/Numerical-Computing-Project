class SignificantFigures:
    __value = 0
    
    def __init__(self, value:str):
        self.__checkSignificantFigures(value)
    
    def __checkSignificantFigures(self, value:str) -> None:
        self.__validateValue(value)
        
        significantFigures:int = 0
        
        for char in value:
            if (char == "0" and significantFigures == 0):
                continue
            elif (char != "."):
                significantFigures += 1
    
        self.__value = significantFigures

    def __validateValue(self, value:str) -> None:
        if (isinstance(value, str)):
            validValues = "-.0123456789abcdefABCDEF"
            numberOfPoints = 0
            for char in value:
                if (char not in validValues):
                    raise ValueError("Error: El valor ingresado posee caracteres no válidos")
                elif (char == "." and numberOfPoints == 1):
                    raise ValueError("Error: El formato del número con punto decimal es incorrecto")
                elif (char == "."): 
                    numberOfPoints += 1
        else:
            raise ValueError("Error: El valor ingresado debe ser un string")

    def getValue(self):
        return self.__value
    
    def __str__(self):
        return f"{self.__value}"
