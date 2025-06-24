from Process.EquationSolver.AbstractEquationSolver import AbstractEquationSolver
from Process.MatrixOperators.MatrixOperations import MatrixOperations
from Process.MatrixOperators.MatrixDimensionsOperations import MatrixDimensionsOperations


class MatrixEquationSolver(AbstractEquationSolver):
    def __init__(self):
        self.matrixOperator = MatrixDimensionsOperations()

        super().__init__()
        self.operators = {
            '+': lambda x, y: self.matrixOperator.determineDimensionsOfAddition(x.shape, y.shape),
            '-': lambda x, y: self.matrixOperator.determineDimensionsOfSubstraction(x.shape, y.shape),
            '*': lambda x, y: self.matrixOperator.determineDimensionsOfMultiplication(x.shape, y.shape),
        }
        self.precedences = {
            '+': 1,
            '-': 1,
            '*': 2,
        }

    def _evaluateOperator(self, operator, operand1, operand2):
        if operator not in self.operators:
            raise ValueError(f"Error: Operador desconocido: {operator}")
        return self.operators[operator](operand1, operand2)

    def _getOperatorPrecedence(self, operator):
        if operator not in self.precedences:
            raise ValueError(f"Error: Precedencia desconocida para el operador: {operator}")
        return self.precedences[operator]