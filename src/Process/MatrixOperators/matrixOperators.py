import numpy as np
class matrixOperator:

    def __init__(self):
       pass

    def calculateTranspose(self, matrix : np.ndarray) -> np.ndarray:
        transpose = np.zeros((len(matrix), len(matrix[0])), dtype=np.float64)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                transpose[j][i] = matrix[i][j]
        return transpose