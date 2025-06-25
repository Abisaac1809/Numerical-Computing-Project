import numpy as np
from Validations.MatrixValidator import MatrixValidator
from Helpers.ErrorHandling.Exceptions import *

class MatrixOperations:
    def __init__(self):
        self.validator = MatrixValidator()
    
    def add(self, matrixA, matrixB):
        if not self.validator.canAddOrSubtract(matrixA, matrixB):
            raise ValueError("Las matrices no tienen las mismas dimensiones")
        
        result = np.zeros((matrixA.shape[0], matrixA.shape[1]))
        for i in range(matrixA.shape[0]):
            for j in range(matrixA.shape[1]):
                result[i, j] = matrixA[i, j] + matrixB[i, j]
        return result
    
    def subtract(self, matrixA, matrixB):
        if not self.validator.canAddOrSubtract(matrixA, matrixB):
            raise ValueError("Las matrices no tienen las mismas dimensiones")
        
        result = np.zeros((matrixA.shape[0], matrixA.shape[1]))
        for i in range(matrixA.shape[0]):
            for j in range(matrixA.shape[1]):
                result[i, j] = matrixA[i, j] - matrixB[i, j]
        return result
    
    def multiply(self, matrixA, matrixB):
        if not self.validator.canMultiply(matrixA, matrixB):
            raise ValueError("Número de columnas de A debe coincidir con filas de B")
        
        result = np.zeros((matrixA.shape[0], matrixB.shape[1]))
        for i in range(matrixA.shape[0]):
            for j in range(matrixB.shape[1]):
                sum_val = 0
                for k in range(matrixA.shape[1]):
                    sum_val += matrixA[i, k] * matrixB[k, j]
                result[i, j] = sum_val
        return result
    
    def scalarMultiply(self, matrix, scalar):
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
        if not self.validator.canInvert(matrix):
            raise ValueError("Matriz no es cuadrada o es singular")
        
        n = matrix.shape[0]
        det = self.validator._determinant(matrix)
        
        if n == 1:
            return np.array([[1 / matrix[0, 0]]])
        cofactors = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                minor = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
                cofactor = (-1) ** (i + j) * self.validator._determinant(minor)
                cofactors[i, j] = cofactor

        adjugate = self.transpose(cofactors)

        inverse = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                inverse[i, j] = adjugate[i, j] / det
        
        return inverse