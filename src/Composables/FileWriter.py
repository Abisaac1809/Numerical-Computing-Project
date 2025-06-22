import numpy as np
from pathlib import Path
from datetime import datetime
import random  
import time   

class FileWriter:

    def __init__(self):
        self.__resultsDir = Path("Storage/Results")
        self.__resultsDir.mkdir(parents=True, exist_ok=True)
    
    def __generateSerial(self) -> str:
        timestamp = int(time.time() % 1000000)
        random_num = random.randint(0, 0xFFFFFF)
        
        combined = (timestamp << 24) | random_num
        return f"{combined:08x}"
    
    def __getCurrentDate(self) -> str:
        return datetime.now().strftime("%Y%m%d")
    
    def __generateFileName(self, inputSerial: str) -> str:
        currentDate = self.__getCurrentDate()
        newSerial = self.__generateSerial()
        return f"{inputSerial}_{currentDate}_{newSerial}.txt"
    
    def writeResultsToFile(self, dataArray: np.ndarray, inputSerial: str) -> str:
        if not isinstance(dataArray, np.ndarray) or dataArray.size == 0:
            raise ValueError("Los datos deben ser un array numpy no vacío")
            
        fileName = self.__generateFileName(inputSerial)
        filePath = self.__resultsDir / fileName
        
        with open (filePath, "w", encoding="utf-8") as file:
            file.write("Números escaneados:")
            file.write("\n")
            for i in range(len(dataArray)):
                for j in range(len(dataArray[i])):
                    if dataArray[i][j]:
                        file.write(dataArray[i][j].__str__())
