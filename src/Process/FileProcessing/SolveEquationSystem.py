from Process.FileProcessing.FileProcess import FileProcess
from Process.MatrixOperators.SystemOfEquationsSolver import SystemOfEquationsSolver
from Process.Conversions.Conversor import Conversor
from Process.ErrorHandling.ErrorLogger import ErrorLogger
from Process.ErrorHandling.Exceptions import *
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
        augmentedMatrix = self.__convertToFloat(augmentedMatrix)
        coefficients = augmentedMatrix[:, :len(augmentedMatrix)]
        independents = augmentedMatrix[:,-1]
        
        try:
            result = self.__solveSystemOfEquation(coefficients, independents)
        except SystemDontHaveSolution as error:
            print("El sistema de ecuaciones que has ingresado no tiene solución")
            return

        fileWriter.writeSystemOfEquationResult(result, readedFileSerial)

    def __convertToFloat(self, matrix:np.ndarray) -> np.ndarray:
        conversor = Conversor()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if self.__isHexadecimal(matrix[i][j]):
                    try:
                        matrix[i][j] = conversor.convertToDecimal(matrix[i][j], 16)
                    except ValueError as error:
                        ErrorLogger.LogError(error)
                matrix[i][j] = float(matrix[i][j])
        return matrix

    def __isHexadecimal(self, value:str) -> bool:
        letters = "abcdefABCDEF"
        for char in value:
            if char in letters:
                return True
        return False
    
    def __solveSystemOfEquation(self, coefficients:np.ndarray, independents:np.ndarray) -> np.ndarray:
        try:
            return self.matrixOperator.solveSystemOfEquation(coefficients, independents)
        except SystemDontHaveSolution as error:
            raise SystemDontHaveSolution("Error: El sistema de ecuaciones no tiene una solución")
        except Exception as error:
            ErrorLogger.LogError(error)