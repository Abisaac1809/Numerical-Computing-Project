import numpy as np
from Validations.MatrixValidator import MatrixValidator
from Process.ErrorHandling.Exceptions import *

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
    
    def transpose(self, matrix):
        result = np.zeros((matrix.shape[1], matrix.shape[0]))
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                result[j, i] = matrix[i, j]
        return result

    def inverse(self, matrix):
        if not self.validator.can_invert(matrix):
            raise ValueError("Matriz no es cuadrada o es singular")
        
        n = matrix.shape[0]
        det = self.validator._determinant(matrix)
        
        if n == 1:
            return np.array([[1 / matrix[0, 0]]])
        
        # Matriz de cofactores
        cofactors = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                minor = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
                cofactor = (-1) ** (i + j) * self.validator._determinant(minor)
                cofactors[i, j] = cofactor
        
        # Adjunta (transpuesta de cofactores)
        adjugate = self.transpose(cofactors)
        
        # Inversa (adjunta/determinante)
        inverse = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                inverse[i, j] = adjugate[i, j] / det
        
        return inverse