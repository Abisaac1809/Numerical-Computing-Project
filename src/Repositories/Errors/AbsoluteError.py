class AbsoluteError:
    __value:float = 0.0
    
    def __init__(self, exactValue:float, aproximatedValue:float):
        if (not self.__floatIsValid(exactValue) and not self.__floatIsValid(aproximatedValue)):
            raise ValueError("Error: Solo se aceptan valores float")
        
        self._calculateAndSetAbsoluteError(exactValue, aproximatedValue)
    
    def _calculateAndSetAbsoluteError(self, exactValue:float, aproximatedValue:float) -> None:
        self.__value = exactValue - aproximatedValue
    
    def getValue(self) -> float:
        return self.__value
        
    def __str__(self) -> str:
        return f"Error Absoluto: {self.__value} unidades"
    
    def __floatIsValid(self, value:float) -> bool:
        try:
            float(value)
            return True
        except (TypeError, ValueError):
            return False
