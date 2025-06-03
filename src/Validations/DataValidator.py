import numpy as np

class DataValidator:
    def validateInt(self, value:str, limit:int) -> int:
        while (True):
            try:
                number = int(value)
                if (number > 0 and number <= limit):
                    return number
                else:
                    value = input("Ingresa un número válido: ")
            except (ValueError):
                print("Error: El número que has ingresado es inválido")
                value = input("Ingresa un número válido: ")
    
    def chooseOptionOf(self, optionsArray:np.ndarray, text:str) -> int:
        option:int
        
        for i in range(len(optionsArray)):
            print(f"{i+1}. {optionsArray[i]}")
        
        option = self.validateInt(text, len(optionsArray))

        return option - 1