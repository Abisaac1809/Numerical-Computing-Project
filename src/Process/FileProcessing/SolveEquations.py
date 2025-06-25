from Helpers.FileReader import FileReader
from Composables.FileWriter import FileWriter
from Process.EquationSolver.BasicEquationSolver import BasicEquationSolver
from Process.FileProcessing.FileProcess import FileProcess
from Helpers.Conversions.Conversor import Conversor
from Helpers.ErrorHandling.Exceptions import *
from Helpers.ErrorHandling.ErrorLogger import ErrorLogger
from Validations.DataValidator import DataValidator
from Structures.LinkedList import LinkedList
import numpy as np

class SolveEquations(FileProcess):
    def execute(self):
        self.dataValidator = DataValidator()
        self.basicEquationSolver = BasicEquationSolver()
        fileReader = FileReader()
        self.fileWriter = FileWriter()
        
        try:
            availableFiles:np.ndarray = fileReader.getFileList()
        except (FileNotFoundError, NotADirectoryError) as error:
            ErrorLogger.LogError(error)
            print(f"Lo sentimos, ha ocurrido un error que impide leer los archivos: {error}")
            return
        
        print("\n\nArchivos disponibles:")
        equationsFilePosition:int = self.dataValidator.chooseOptionOf(availableFiles, "Elige el archivo que contiene las ecuaciones: ")
        equationsFileName:str = availableFiles[equationsFilePosition]
        readedEquationFileSerial:str = equationsFileName.split("_")[2].split(".")[0]
        equations:np.ndarray = fileReader.readBinaryFile(equationsFileName)

        print("\n\nArchivos disponibles:")
        valueFilePosition = self.dataValidator.chooseOptionOf(availableFiles, "Elige el archivo que contiene los valores: ")
        valueFileName = availableFiles[valueFilePosition]
        readedValueFileSerial = valueFileName.split("_")[2].split(".")[0]
        values = fileReader.readBinaryFile(valueFileName)
        
        values = Conversor.convertEveryValueToFloat(values)
        variableNames:LinkedList = self.determineVariableNames(equations)
        variables:dict = self.determineVariables(values, variableNames)
        
        inputSerial = readedEquationFileSerial + readedValueFileSerial
        filePath = self.fileWriter.getFilePath(inputSerial)
        self.fileWriter.writeHeaderAndVariables(filePath, variables)
        self.calculateAndWriteResults(filePath, equations, variables)

        print("Se han calculado con éxito las ecuaciones")
    
    
    def determineVariableNames(self, equations:np.ndarray) -> LinkedList:
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

    def determineVariables(self, values:np.ndarray, variableNames:LinkedList) -> dict:
        if not isinstance(values, np.ndarray):
            raise ValueError("Error: El arreglo con los valores es inválido")
        
        variables = {}
        position = 0
        
        for i in range(len(values)):
            for j in range(len(values[i])):
                if values[i][j]:
                    variables[variableNames.get(position)] = values[i][j]
                    position+=1
        
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
                        result = self.basicEquationSolver.solve(equations[i][j], variables)
                        self.fileWriter.writeEquationAndResult(filePath, equations[i][j], result)
                except ZeroDivisionError as error:
                    errorMessage = "Error: División por cero indefinida: ∄c∈R tal que a=0xc."
                    self.fileWriter.writeEquationAndError(filePath, equations[i][j], str(errorMessage))
                except (InvalidOperators, InvalidBrackets, InvalidEquation):
                    errorMessage = "Error: La ecuación tiene problemas de sintaxis y no se puede resolver"
                    self.fileWriter.writeEquationAndError(filePath, equations[i][j], errorMessage)
                except VariableNotExist as error:
                    errorMessage = "Error: El archivo que has ingresado no tenía valores suficientes para cubrir todas las variables"
                    self.fileWriter.writeEquationAndError(filePath, equations[i][j], errorMessage)
                except Exception as error:
                    ErrorLogger.LogError(error)