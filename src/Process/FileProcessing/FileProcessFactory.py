import numpy as np
from Process.FileProcessing.FileProcess import FileProcess
from Process.FileProcessing.ScanNumbers import ScanNumbers
from Process.FileProcessing.SolveEquationSystem import SolveEquationSystem
from Process.FileProcessing.SolveEquations import SolveEquations
from Process.FileProcessing.SolveMatrixEquations import SolveMatrixEquations


class FileProcessFactory:
    __processes:dict = {
        "Escanear archivo de números" : ScanNumbers,
        "Resolver sistema de ecuaciones" : SolveEquationSystem,
        "Resolver ecuaciones" : SolveEquations,
        "Resolver ecuaciones con matrices" : SolveMatrixEquations
    }
    
    def getAvailableProcesses(self) -> np.ndarray:
        return np.array(list(self.__processes.keys()))
    
    def getProcess(self, process:str) -> FileProcess:
        if (process not in self.__processes):
            raise ValueError("Error: Has solicitado un proceso que no existe")
        return self.__processes[process]()