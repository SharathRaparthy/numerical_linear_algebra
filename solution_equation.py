import numpy as np

# Diagonal matrix
def diagonal_solution(matrixA, matrixB):
    heightB, widthB = matrixB.shape
    matrixX = np.zeros((heightB, widthB))
    lengthA = len(matrixA[0])
    for i in range(lengthA):
        matrixX[i] = matrixB[i]/matrixA[i][i]
    return matrixX
matA = np.array([[2,0,0],[0,3,0],[0,0,4]])
matB = np.array([[1],[2],[1]])
solutionX = diagonal_solution(matA,matB)

print(solutionX)

def lower_traingle(matrixA, matrixB):
    heightB, widthB = matrixB.shape
    matrixX = np.zeros((heightB, widthB))
    matrixX[0] = matrixB[0]/matrixA[0][0]
    for i in range(1, len(matrixA[0])):
        sum = 0
        for j in range(i):
            sum = sum + matrixA[i][j]*matrixX[j]
        matrixX[i] = (matrixB[i] - sum)/matrixA[i][i]
    return matrixX

matlA = np.array([[1,0,0],[1,2,0],[3,2,5]])
matlB = np.array([[3],[2],[4]])
solution1X = lower_traingle(matlA, matlB)
print(solution1X)

def upper_traingle(matrixA, matrixB):
    heightB, widthB = matrixB.shape
    matrixX = np.zeros((heightB, widthB))
    length = len(matrixA[0])

    matrixX[length-1] = matrixB[length-1]/matrixA[length-1][length-1]
    for i in reversed(range(length)):
        sum = 0
        for j in range(i+1, length):
            sum += matrixA[i][j]*matrixX[j]
        matrixX[i] = (matrixB[i] - sum)/matrixA[i][i]
    return matrixX
matlA = np.array([[3,2,5],[0,2,1],[0,0,2]])
matlB = np.array([[3],[2],[4]])
solution_uX = upper_traingle(matlA, matlB)
print(solution_uX)

def unitary_matrix(matrixA, matrixB):
    heightB, widthB = matrixB.shape
    trans_A = matrixA.transpose()
    matrixX = trans_A.dot(matrixB)
    return matrixX
mat_uniA = np.array([[5,-2,2,7],[1,0,0,3],[-3,1,5,0],[3,-1,-9,4]])
mat_uniB = np.array([[1],[2],[3],[4]])
matX = unitary_matrix(mat_uniA, mat_uniB)
print(matX)
