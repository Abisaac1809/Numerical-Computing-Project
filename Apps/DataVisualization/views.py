from django.shortcuts import render
from Apps.Common.Composables.MatrixEquationGenerator import MatrixEquationGenerator
from django.http import JsonResponse
from Apps.NumericalMethods.Solvers.EquationSolvers.MatrixEquationSolver import MatrixEquationSolver
from Apps.Common.Composables.DataGenerate import archiveGenerator
from Apps.NumericalMethods.Solvers.MatrixOperators.SystemOfEquationsSolver import SystemOfEquationsSolver
from Apps.Common.Repositories.DataModels.Point import Point
from Apps.DataVisualization.Methods.GraphVisualizer import GraphVisualizer
import numpy as np
from .Methods.RandomGraphUtils import *

def generateRandomGraphAndPoints(request):
    generator = archiveGenerator()
    equationSolver = MatrixEquationSolver()
    gaussSolver = SystemOfEquationsSolver()
    variableNames = ['A', 'B', 'C']

    matrixFiles: list[str] = generateMatrixFiles(generator, 3)
    MatrixEquationGenerator.generateComplexFormulas()

    matrixs: dict[str, np.ndarray] = loadMatrices(variableNames, matrixFiles)
    formulas: list[str] = loadFormulas("MatrixFormulas.txt")

    equationResults: list[np.ndarray] = resolveMatrixFormulas(equationSolver, formulas, matrixs)
    points: list[Point] = solvePoints(gaussSolver, equationResults, variableNames)
    setPointsGroup(points)
    image: str = GraphVisualizer.plotPointsAndDistances3D(points)
    print(image)
    return render(request, 'index.html')
