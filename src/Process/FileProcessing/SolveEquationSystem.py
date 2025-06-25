from Process.FileProcessing.FileProcess import FileProcess
from Process.MatrixOperators.SystemOfEquationsSolver import SystemOfEquationsSolver
from Helpers.Conversions.Conversor import Conversor
from Helpers.ErrorHandling.ErrorLogger import ErrorLogger
from Helpers.ErrorHandling.Exceptions import *
from Helpers.FileReader import FileReader
from Composables.FileWriter import FileWriter
from Validations.DataValidator import DataValidator
import numpy as np

class SolveEquationSystem(FileProcess):
    def execute(self):
        self.dataValidator = DataValidator()
        self.matrixOperator = SystemOfEquationsSolver()
        fileWriter = FileWriter()
        fileReader = FileReader()
        try:
            availableFiles:np.ndarray = fileReader.getFileList()
        except (FileNotFoundError, NotADirectoryError) as error:
            ErrorLogger.LogError(error)
            print(f"Lo sentimos, ha ocurrido un error que impide realizar la operación: {error}")
            return
        
        print("Archivos disponibles para escanear\n")
        filePosition = self.dataValidator.chooseOptionOf(availableFiles, "Ingresa el archivo que quieres escanear: ")
        
        fileName = availableFiles[filePosition]
        readedFileSerial = fileName.split("_")[2].split(".")[0]
        augmentedMatrix = fileReader.readBinaryFile(fileName)
        augmentedMatrix = Conversor.convertEveryValueToFloat(augmentedMatrix)
        coefficients = augmentedMatrix[:, :len(augmentedMatrix)]
        independents = augmentedMatrix[:,-1]
        
        try:
            result = self.__solveSystemOfEquation(coefficients, independents)
        except SystemDontHaveSolution as error:
            print("El sistema de ecuaciones que has ingresado no tiene solución")
            return

        fileWriter.writeSystemOfEquationResult(result, readedFileSerial)
    
    def __solveSystemOfEquation(self, coefficients:np.ndarray, independents:np.ndarray) -> np.ndarray:
        try:
            return self.matrixOperator.solveSystemOfEquation(coefficients, independents)
        except SystemDontHaveSolution as error:
            raise SystemDontHaveSolution("Error: El sistema de ecuaciones no tiene una solución")
        except Exception as error:
            ErrorLogger.LogError(error)