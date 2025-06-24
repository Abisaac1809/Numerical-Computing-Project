class MatrixDimensionsOperations:

    def determineDimensionsOfAddition(self, matrix1_dims, matrix2_dims):
        rows1, cols1 = matrix1_dims
        rows2, cols2 = matrix2_dims

        if rows1 != rows2 or cols1 != cols2:
            raise ValueError(f"No se puede realizar la suma: matriz {matrix1_dims} + matriz {matrix2_dims}. "
                           f"Las dimensiones deben ser iguales.")

        return (rows1, cols1)

    def determineDimensionsOfSubstraction(self, matrix1_dims, matrix2_dims):
        rows1, cols1 = matrix1_dims
        rows2, cols2 = matrix2_dims
        if rows1 != rows2 or cols1 != cols2:
            raise ValueError(f"No se puede realizar la resta: matriz {matrix1_dims} - matriz {matrix2_dims}. "
                           f"Las dimensiones deben ser iguales.")
        return (rows1, cols1)

    def determineDimensionsOfMultiplication(self, matrix1_dims, matrix2_dims):
        rows1, cols1 = matrix1_dims
        rows2, cols2 = matrix2_dims
        if cols1 != rows2:
            raise ValueError(f"No se puede realizar la multiplicación: matriz {matrix1_dims} × matriz {matrix2_dims}. "
                           f"El número de columnas de la primera matriz ({cols1}) debe ser igual "
                           f"al número de filas de la segunda matriz ({rows2}).")
        return (rows1, cols2)