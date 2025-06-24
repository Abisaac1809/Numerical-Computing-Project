import numpy as np

class MatrixValidator:
    def canAddOrSubtract(self, matrix_a, matrix_b):
        """Valida si dos matrices pueden ser sumadas o restadas"""
        return matrix_a.shape == matrix_b.shape
    
    def canMultiply(self, matrix_a, matrix_b):
        """Valida si dos matrices pueden ser multiplicadas"""
        return matrix_a.shape[1] == matrix_b.shape[0]
    
    def can_transpose(self, matrix):
        """Valida si una matriz puede ser transpuesta (siempre posible)"""
        return True
    
    def canInvert(self, matrix):
        """Valida si una matriz puede ser invertida"""
        return matrix.shape[0] == matrix.shape[1] and not np.isclose(np.linalg.det(matrix), 0)
