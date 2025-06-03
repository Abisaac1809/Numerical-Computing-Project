import numpy as np
from Process.FileProcessing.FileProcessFactory import FileProcessFactory
from Process.FileProcessing.FileProcess import FileProcess
from Validations.DataValidator import DataValidator

def main():
    dataValidator:DataValidator
    processesFactory:FileProcessFactory
    availableProcesses:np.ndarray
    process:FileProcess
    numberOfProcess:int 
    
    dataValidator = DataValidator()
    processesFactory = FileProcessFactory()
    
    print("Bienvenido a Numerical Computing Project\n")
    print("Procesos disponibles\n")
    
    availableProcesses = processesFactory.getAvailableProcesses()

    numberOfProcess = dataValidator.chooseOptionOf(availableProcesses, "Ingresa el proceso que quieres realizar: ")
    
    process = processesFactory.getProcess(availableProcesses[numberOfProcess])
    process.execute()

main()