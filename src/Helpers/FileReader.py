import numpy as np
from pathlib import Path

class FileReader:
    
    def __init__(self):
        self.__binaryFilesDir = Path("Storage/BinaryFiles")
        self.__binaryFilesDir.mkdir(parents=True, exist_ok=True)
    
    def getRowCount(self, fileName: str) -> int:
        filePath = self.__binaryFilesDir / fileName
        if not filePath.exists():
            raise FileNotFoundError(f"Archivo {fileName} no encontrado")
            
        with open(filePath, 'rb') as file:
            return file.read().count(b'#') + 1
    
    def getColumnCount(self, fileName: str) -> int:
        filePath = self.__binaryFilesDir / fileName
        if not filePath.exists():
            raise FileNotFoundError(f"Archivo {fileName} no encontrado")
            
        with open(filePath, 'rb') as file:
            first_line = file.readline().split(b'#')[0]
            return len(first_line.split())
    
    def readBinaryFile(self, fileName: str) -> np.ndarray:
        filePath = self.__binaryFilesDir / fileName
        if not filePath.exists():
            raise FileNotFoundError(f"Archivo {fileName} no encontrado")
        
        rows = self.getRowCount(fileName)
        cols = self.getColumnCount(fileName)
        
        result_array = np.empty((rows, cols), dtype='object')
        
        with open(filePath, 'rb') as file:
            content = file.read().decode('utf-8')
            row_data = content.split('#')
            
            for i in range(rows):
                if i < len(row_data):
                    numbers = row_data[i].strip().split()
                    for j in range(cols):
                        if j < len(numbers):
                            result_array[i, j] = numbers[j]
                        else:
                            result_array[i, j] = ''
                else:
                    result_array[i, :] = ''
        
        return result_array