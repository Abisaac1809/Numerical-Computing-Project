from Helpers.FileReader import FileReader
from Composables.FileWriter import FileWriter
from Process.EquationSolver.MatrixEquationSolver import MatrixEquationSolver
from Process.EquationSolver.DimensionsEquationSolver import DimensionsEquationSolver
from Process.FileProcessing.FileProcess import FileProcess
from Process.Conversions.Conversor import Conversor
from Process.ErrorHandling.Exceptions import *
from Process.ErrorHandling.ErrorLogger import ErrorLogger
from Validations.DataValidator import DataValidator
from Structures.LinkedList import LinkedList
import numpy as np

class SolveMatrixEquations(FileProcess):
    def execute(self):
        self.dataValidator = DataValidator()
        self.dimensionsEquationSolver = DimensionsEquationSolver()
        self.matrixEquationSolver = MatrixEquationSolver()
        self.fileReader = FileReader()
        self.fileWriter = FileWriter()
        
        try:
            availableFiles:np.ndarray = self.fileReader.getFileList()
        except (FileNotFoundError, NotADirectoryError) as error:
            ErrorLogger.LogError(error)
            print(f"Lo sentimos, ha ocurrido un error que impide leer los archivos: {error}")
            return
        
        print("\n\nArchivos disponibles:")
        equationsFilePosition:int = self.dataValidator.chooseOptionOf(availableFiles, "Elige el archivo que contiene las ecuaciones: ")
        equationsFileName:str = availableFiles[equationsFilePosition]
        readedEquationFileSerial:str = equationsFileName.split("_")[2].split(".")[0]
        equations:np.ndarray = self.fileReader.readBinaryFile(equationsFileName)
        filePath:str = self.fileWriter.getFilePath(readedEquationFileSerial)

        variableNames:LinkedList = self.determineNameOfVariables(equations)
        variables = self.determinateVariables(availableFiles, variableNames)
        
        for matrix in variables.values():
            Conversor.convertEveryValueToFloat(matrix)
        
        self.fileWriter.writeHeaderAndVariables(filePath, variables)
        self.calculateAndWriteResults(filePath, equations, variables)

        print("Se han calculado con éxito las ecuaciones")
    
    
    def determineNameOfVariables(self, equations:np.ndarray) -> LinkedList:
        if not isinstance(equations, np.ndarray):
            raise ValueError("Error: El arreglo con las ecuaciones es inválido")
        
        availableVariableNames = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        variableNamesReaded = set()
        variableNames = LinkedList()
        
        for i in range(len(equations)):
            for j in range(len(equations[0])):
                if equations[i][j]:
                    for char in equations[i][j]:
                        if char in availableVariableNames and char not in variableNamesReaded:
                            variableNames.addLast(char)
                            variableNamesReaded.add(char)
        
        return variableNames

    def determinateVariables(self, availableFiles:np.ndarray, variableNames:LinkedList) -> dict:
        
        variables = {}
        
        for i in range(variableNames.getSize()):
            name = variableNames.get(i)
            print("\n\nArchivos disponibles:\n")
            matrixFilePosition = self.dataValidator.chooseOptionOf(availableFiles, f"Ingresa el archivo que contiene la matriz {name}: ")
            matrixFileName = availableFiles[matrixFilePosition]
            matrix = self.fileReader.readBinaryFile(matrixFileName)
            variables[name] = matrix
        return variables
    
    def calculateAndWriteResults(self, filePath:str, equations:np.ndarray, variables:dict):
        if not isinstance(equations, np.ndarray) or not isinstance(variables, dict):
            ValueError("Error: El arreglo de ecuaciones y de variables son inválidos")
        
        if len(equations) < 1:
            raise ValueError("Error: No hay ecuaciones para resolver")
        
        for i in range(len(equations)):
            for j in range(len(equations[i])):
                try:
                    if equations[i][j]:
                        self.dimensionsEquationSolver.solve(equations[i][j], variables)
                        result = self.matrixEquationSolver.solve(equations[i][j], variables)
                        self.fileWriter.writeEquationAndResult(filePath, equations[i][j], result)
                except ImposibleMatrixOperation as error:
                    self.fileWriter.writeEquationAndError(filePath, equations[i][j], str(error))
                except (InvalidOperators, InvalidBrackets, InvalidEquation):
                    errorMessage = "Error: La ecuación tiene problemas de sintaxis y no se puede resolver"
                    self.fileWriter.writeEquationAndError(filePath, equations[i][j], errorMessage)
                except Exception as error:
                    ErrorLogger.LogError(error)