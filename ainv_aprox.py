import numpy as np

def inv_aprox(matrixA):
    length = len(matrixA[0])
    x = np.ones((length,1))
    y = np.ones((length,1))
    y[0] = 1/matrixA[0][0]
    for j in range(1,length):
        s = 0
        for k in range(j):
            s += matrixA[j][k]*y[k]
        sign_s = s/np.abs(s)
        y[j] = -(s + sign_s)/matrixA[j][j]
    y_norm = np.sqrt(np.sum(np.multiply(y,y)))
    norm_A = y_norm/np.sqrt(length)
    return norm_A
matA = np.array([[2,0,0],[5,4,0],[3,1,6]])
norm = inv_aprox(matA)
print(norm)
