import os
import numpy as np
from pathlib import Path

class FileReader:
    
    def __init__(self):
        self.__binaryFilesDir = Path("Storage/BinaryFiles")
        self.__binaryFilesDir.mkdir(parents=True, exist_ok=True)
    
    def getFileList(self) -> np.ndarray:
        try:
            directories:np.ndarray = np.array(os.listdir(self.__binaryFilesDir) )

            if (len(directories) > 0):
                return directories
            else:
                raise FileNotFoundError("No se encontraron archivos.")

        except FileNotFoundError as e:
            print("Manage-Error: Directorio no existe: ", e)
            return None

        except NotADirectoryError as e:
            print("Manage-Error: Ocurrió un error inesperado:", e)
            return None
    
    def getRowCount(self, fileName: str) -> int:
        filePath = self.__binaryFilesDir / fileName
        if not filePath.exists():
            raise FileNotFoundError(f"Archivo {fileName} no encontrado")
            
        with open(filePath, 'rb') as file:
            return len(file.readlines())
    
    def getColumnCount(self, fileName: str) -> int:
        filePath = self.__binaryFilesDir / fileName
        if not filePath.exists():
            raise FileNotFoundError(f"Archivo {fileName} no encontrado")
        
        maxColumns:int = 0
        
        with open(filePath, 'rb') as file:
            for line in file:
                cleanLine = line.decode("utf-8")
                if not cleanLine:
                    continue

                columns:list = cleanLine.split('#')
                currentColumns = len(columns)

                if currentColumns > maxColumns:
                    maxColumns = currentColumns

            return maxColumns
    
    def readBinaryFile(self, fileName: str) -> np.ndarray:
        filePath = self.__binaryFilesDir / fileName
        if not filePath.exists():
            raise FileNotFoundError(f"Archivo {fileName} no encontrado")
        
        rows = self.getRowCount(fileName)
        cols = self.getColumnCount(fileName)
        
        result_array = np.empty((rows, cols), dtype='object')
        
        with open(filePath, 'rb') as file:
            i = 0
            line = file.readline().decode("utf-8")
            while (line):
                content = line.split("#")
                
                for j in range(len(content)):
                    if (len(content[j]) == 0):
                        continue
                    result_array[i][j] = content[j]
                
                i += 1
                line = file.readline().decode("utf-8")

        return result_array