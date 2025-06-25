from Process.FileProcessing.FileProcess import FileProcess
from Process.ErrorHandling.Exceptions import *
from Process.ErrorHandling.ErrorLogger import ErrorLogger
from Repositories.StudiedNumbers.StudiedNumber import StudiedNumber
from Helpers.FileReader import FileReader
from Composables.FileWriter import FileWriter
from Validations.DataValidator import DataValidator
import numpy as np

class ScanNumbers(FileProcess):
    def execute(self):
        dataValidator = DataValidator()
        fileWriter = FileWriter()
        fileReader = FileReader()
        
        try:
            availableFiles:np.ndarray = fileReader.getFileList()
        except (FileNotFoundError, NotADirectoryError) as error:
            ErrorLogger.LogError(error)
            print(f"Lo sentimos, ha ocurrido un error que impide realizar la operación: {error}")
            return
        
        print("Archivos disponibles para escanear\n")
        filePosition = dataValidator.chooseOptionOf(availableFiles, "Ingresa el archivo que quieres escanear: ")
        
        fileName = availableFiles[filePosition]
        readedFileSerial = fileName.split("_")[2].split(".")[0]
        scannedValues = fileReader.readBinaryFile(fileName)
    
        numbers = np.empty((len(scannedValues), len(scannedValues[0])), dtype='object')

        self.__fillNumbersArray(numbers, scannedValues)
        fileWriter.writeResultsToFile(numbers, readedFileSerial)
        
        print("Se ha escaneado con éxito el archivo")

    def __fillNumbersArray(self, numbers:np.ndarray, scannedValues:np.ndarray) -> None:
        for i in range(len(scannedValues)):
            for j in range(len(scannedValues[i])):
                try:
                    if scannedValues[i][j]:
                        numbers[i][j] = StudiedNumber(scannedValues[i][j].strip())
                except NumberIsInvalid:
                    numbers[i][j] = f"\n{scannedValues[i][j]}: Es un valor inválido\n"
                except NoneType:
                    continue
                except (ValueError, TypeError) as error:
                    ErrorLogger.LogError(error)
