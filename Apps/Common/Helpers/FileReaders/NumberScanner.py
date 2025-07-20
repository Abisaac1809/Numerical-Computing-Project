
from Common.Helpers.ErrorHandling.Exceptions import *
from Common.Helpers.ErrorHandling.ErrorLogger import ErrorLogger
from Common.Repositories.StudiedNumbers.StudiedNumber import StudiedNumber
from Apps.Common.Helpers.FileReaders.FileReader import FileReader
from Common.Composables.FileWriter import FileWriter
import numpy as np

class NumberScanner:
    def scanAnalizeAndWriteResults(self, fileName:str) -> None:
        fileWriter = FileWriter()
        fileReader = FileReader()
        
        readedFileSerial = fileName.split("_")[2].split(".")[0]
        scannedValues = fileReader.readBinaryFile(fileName)

        numbers = np.empty((len(scannedValues), len(scannedValues[0])), dtype="object")

        self.__fillNumbersArray(numbers, scannedValues)
        fileWriter.writeResultsToFile(numbers, readedFileSerial)

    def __fillNumbersArray(
        self, numbers: np.ndarray, scannedValues: np.ndarray) -> None:
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
