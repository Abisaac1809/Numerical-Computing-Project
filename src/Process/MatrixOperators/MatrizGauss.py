import numpy as np

class MatrizGauss:
    def __init__(self, matriz_A, vector_b):
        self.A = np.array(matriz_A, dtype=float)
        self.b = np.array(vector_b, dtype=float)
        
    def gauss_jordan(self):
        n = len(self.b)
        Ab = np.hstack((self.A, self.b.reshape(-1, 1)))
        
        for i in range(n):
            max_row = i
            for k in range(i + 1, n):
                if abs(Ab[k, i]) > abs(Ab[max_row, i]):
                    max_row = k
            Ab[[i, max_row]] = Ab[[max_row, i]]
            
            pivot = Ab[i, i]
            if pivot == 0:
                raise ValueError("La matriz es singular y no puede resolverse.")
            
            Ab[i, i:] /= pivot
            
            for k in range(n):
                if k != i:
                    factor = Ab[k, i]
                    Ab[k, i:] -= factor * Ab[i, i:]
        
        return Ab[:, -1]