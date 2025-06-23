from Process.FileProcessing.FileProcess import FileProcess
from Process.MatrixOperators.SystemOfEquationsSolver import SystemOfEquationsSolver
from Process.Conversions.Conversor import Conversor
from Helpers.FileReader import FileReader
from Composables.FileWriter import FileWriter
from Validations.DataValidator import DataValidator
import numpy as np

class SolveEquationSystem(FileProcess):
    def execute(self):
        dataValidator = DataValidator()
        matrixOperator = SystemOfEquationsSolver()
        fileWriter = FileWriter()
        fileReader = FileReader()
        availableFiles:np.ndarray = fileReader.getFileList()
        
        print("Archivos disponibles para escanear\n")
        filePosition = dataValidator.chooseOptionOf(availableFiles, "Ingresa el archivo que quieres escanear: ")
        
        fileName = availableFiles[filePosition]
        readedFileSerial = fileName.split("_")[2].split(".")[0]
        augmentedMatrix = fileReader.readBinaryFile(fileName)
        augmentedMatrix = self.convertToFloat(augmentedMatrix)

        coefficients = augmentedMatrix[:, :len(augmentedMatrix)]
        independents = augmentedMatrix[:,-1]
        
        result = matrixOperator.solveSystemOfEquation(coefficients, independents)
        fileWriter.writeSystemOfEquationResult(result, readedFileSerial)

    def convertToFloat(self, matrix:np.ndarray) -> np.ndarray:
        conversor = Conversor()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if self.__isHexadecimal(matrix[i][j]):
                    matrix[i][j] = conversor.convertToDecimal(matrix[i][j], 16)
                matrix[i][j] = float(matrix[i][j])
        return matrix

    def __isHexadecimal(self, value:str) -> bool:
        letters = "abcdefABCDEF"
        for char in value:
            if char in letters:
                return True
        return False