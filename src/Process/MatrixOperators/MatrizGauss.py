import numpy as np

class MatrizGauss:
    def __init__(self, matriz_A, vector_b):
        self.A = np.array(matriz_A, dtype=float)
        self.b = np.array(vector_b, dtype=float)
        
    def seleccionar_metodo():
        print("Métodos disponibles:")
        print("1. Gauss-Jordan (Eliminación directa)")
        print("2. Gauss-Seidel (Iterativo)")
        opcion = input("Seleccione el método (1 o 2): ").strip()
        while opcion not in ["1", "2"]:
            print("¡Opción inválida! Intente nuevamente.")
            opcion = input("Seleccione el método (1 o 2): ").strip()
        return opcion

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

    def gauss_seidel(self, tol=1e-6, max_iter=1000):
        n = len(self.b)
        x = np.zeros(n)
        
        for _ in range(max_iter):
            x_prev = x.copy()
            for i in range(n):
                sum1 = 0.0
                for j in range(i):
                    sum1 += self.A[i, j] * x[j]
                
                sum2 = 0.0
                for j in range(i + 1, n):
                    sum2 += self.A[i, j] * x_prev[j]
                
                x[i] = (self.b[i] - sum1 - sum2) / self.A[i, i]
            
            error = 0.0
            for i in range(n):
                error += (x[i] - x_prev[i]) ** 2
            error = error ** 0.5
            
            if error < tol:
                return x
        
        print(f"Gauss-Seidel no convergió después de {max_iter} iteraciones.")
        return x