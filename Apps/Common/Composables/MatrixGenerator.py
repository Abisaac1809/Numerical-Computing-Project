import os
import random

class MatrixGenerator:
    @staticmethod
    def generateComplexFormulas(fileName="MatrixFormulas.txt", outputPath=None, numFormulas=3):
        outputPath = outputPath or os.getcwd()
        fullPath = os.path.join(outputPath, fileName)
        
        if not os.path.exists(outputPath):
            raise FileNotFoundError(f"El directorio {outputPath} no existe")
        
        matrices = ['A', 'B', 'C']
        operations = ['+', '-', '*']
        
        formulas = []
        for _ in range(numFormulas):
            num_terms = random.randint(2, 4)
            
            formula_parts = []
            for i in range(num_terms):
                if random.random() < 0.3 and i > 0:
                    scalar = random.randint(2, 5)
                    formula_parts.append(f"{scalar}")
                
                matrix = random.choice(matrices)
                formula_parts.append(matrix)
                
                if i < num_terms - 1:
                    op = random.choice(operations)
                    formula_parts.append(op)
            
            formula = ' '.join(formula_parts)
            if formula not in formulas:
                formulas.append(formula)
            else:
                numFormulas += 1
        
        try:
            with open(fullPath, 'w') as file:
                file.write("Fórmulas Matriciales Complejas:\n\n")
                for i, formula in enumerate(formulas[:numFormulas], 1):
                    file.write(f"{i}. {formula}\n")
            
            print(f"✓ Archivo generado con éxito en: {fullPath}")
            return fullPath
            
        except Exception as e:
            print(f"✗ Error al generar archivo: {e}")
            return None

if __name__ == "__main__":
    MatrixGenerator.generateComplexFormulas(
        fileName="MisFormulas.txt",
        outputPath="C:\\Users\\HP0246\\Desktop",
        numFormulas=3
    )