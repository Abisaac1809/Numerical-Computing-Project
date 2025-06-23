import numpy as np
from Validations.MatrixValidator import MatrixValidator

class MatrixOperations:
    def __init__(self):
        self.validator = MatrixValidator()
    
    def add(self, matrix_a, matrix_b):
        if not self.validator.can_add_or_subtract(matrix_a, matrix_b):
            raise ValueError("Las matrices no tienen las mismas dimensiones")
        
        result = np.zeros((matrix_a.shape[0], matrix_a.shape[1]))
        for i in range(matrix_a.shape[0]):
            for j in range(matrix_a.shape[1]):
                result[i, j] = matrix_a[i, j] + matrix_b[i, j]
        return result