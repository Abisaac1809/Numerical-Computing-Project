from Process.FileProcessing.FileProcess import FileProcess
from Process.MatrixOperators.SystemOfEquationsSolver import SystemOfEquationsSolver
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

        coefficients = augmentedMatrix[:, :len(augmentedMatrix)]
        independents = augmentedMatrix[:,-1]
        print(coefficients)
        print(independents)
        
        result = matrixOperator.solveSystemOfEquation(coefficients, independents)

        fileWriter.writeSystemOfEquationResult(result, readedFileSerial)