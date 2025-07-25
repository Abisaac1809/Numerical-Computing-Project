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

last_access_times = {}

def data_visualization_view(request):
    client_ip = request.META.get('REMOTE_ADDR')
    current_time = datetime.now()

    # Rate limiting logic
    if client_ip not in last_access_times:
        last_access_times[client_ip] = []
    
    # Remove access times older than 1 minute
    last_access_times[client_ip] = [
        t for t in last_access_times[client_ip] if current_time - t < timedelta(minutes=1)
    ]

    if len(last_access_times[client_ip]) >= 5:
        alert_message = "Access limit exceeded: You can only visit this page 5 times per minute."
        return render(request, 'DataVisualization/data_visualization.html', {'alert_message': alert_message})
    
    last_access_times[client_ip].append(current_time)
    #------------------------------------------------------------------------
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


