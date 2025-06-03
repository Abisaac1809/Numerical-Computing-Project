from Process.FileProcessing.FileProcess import FileProcess
from Repositories.StudiedNumbers.StudiedNumber import StudiedNumber
from Helpers.FileReader import FileReader
from Composables.FileWriter import FileWriter
from Validations.DataValidator import DataValidator
import numpy as np

class ScanNumbers(FileProcess):
    def execute(self):
        scannedValues:np.ndarray[str]
        numbers:np.ndarray[StudiedNumber]
        dataValidator:DataValidator
        fileWriter:FileWriter
        fileReader:FileReader
        availableFiles:np.ndarray
        filePosition:int
        fileName:str
        
        dataValidator = DataValidator()
        fileWriter = FileWriter()
        fileReader = FileReader()
        availableFiles:np.ndarray = fileReader.getFileList()
        
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
                    numbers[i][j] = StudiedNumber(scannedValues[i][j].strip())
                except (ValueError, TypeError, AttributeError) as e:
                    if (scannedValues[i][j]):
                        numbers[i][j] = f"\n{scannedValues[i][j]}: Es un valor inválido\n"
