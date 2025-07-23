import numpy as np
from Apps.Common.Composables.DataGenerate import archiveGenerator
from Apps.Common.Repositories.DataModels.Point import Point  

def generateMatrixFiles(generator: archiveGenerator, count: int) -> list[str]:
    files = []
    for i in range(1, count + 1):
        filename = f"matrix_{i}.txt"
        print(filename)
        generator.setName(filename)
        generator.archiveDataGenerator(3, 4)
        files.append(filename)
    return files

def loadMatrices(variableNames: list[str], matrixFiles: list[str]) -> dict[str, np.ndarray]:
    matrices = {}
    for name, fname in zip(variableNames, matrixFiles):
        matrices[name] = np.loadtxt(fname, delimiter='/')
    return matrices

def loadFormulas(formulaFile: str) -> list[str]:
    with open(formulaFile) as f:
        return [line.strip() for line in f.readlines()]

def resolveMatrixFormulas(equationSolver, formulas: list[str], matrices: dict[str, np.ndarray]) -> list[np.ndarray]:
    results = []
    for formula in formulas:
        result = equationSolver.solve(formula, matrices)
        results.append(result)
    return results

def solvePoints(gaussSolver, equationResults: list[np.ndarray], variableNames: list[str]) -> list[Point]:
    points = []
    for i, matrix in enumerate(equationResults):
        matrixCoefficient = matrix[:, :3]
        vectorIndependent = matrix[:, 3]
        gaussResult = gaussSolver.gaussJordanFullPivoting(matrixCoefficient, vectorIndependent)
        points.append(Point(variableNames[i], gaussResult))
    return points

def setPointsGroup(points: list[Point]):
    for point in points:
        point.setPointGroup(points)