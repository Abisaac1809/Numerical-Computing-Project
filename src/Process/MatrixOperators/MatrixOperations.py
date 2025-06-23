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
    
    def subtract(self, matrix_a, matrix_b):
        if not self.validator.can_add_or_subtract(matrix_a, matrix_b):
            raise ValueError("Las matrices no tienen las mismas dimensiones")
        
        result = np.zeros((matrix_a.shape[0], matrix_a.shape[1]))
        for i in range(matrix_a.shape[0]):
            for j in range(matrix_a.shape[1]):
                result[i, j] = matrix_a[i, j] - matrix_b[i, j]
        return result
    
    def multiply(self, matrix_a, matrix_b):
        if not self.validator.can_multiply(matrix_a, matrix_b):
            raise ValueError("Número de columnas de A debe coincidir con filas de B")
        
        result = np.zeros((matrix_a.shape[0], matrix_b.shape[1]))
        for i in range(matrix_a.shape[0]):
            for j in range(matrix_b.shape[1]):
                sum_val = 0
                for k in range(matrix_a.shape[1]):
                    sum_val += matrix_a[i, k] * matrix_b[k, j]
                result[i, j] = sum_val
        return result
    
    def scalar_multiply(self, matrix, scalar):
        result = np.zeros((matrix.shape[0], matrix.shape[1]))
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                result[i, j] = matrix[i, j] * scalar
        return result