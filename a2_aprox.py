import numpy as np
def aprox(matrixA):
    length = len(matrixA[0])
    x = np.ones((length,1))
    y = np.ones((length,1))
    for j in range(1,length):
        s = 0
        for k in range(j):
            s += matrixA[j][k]*x[k]
        if np.abs(matrixA[j][j] + s) > matrixA[j][j]:
            x[j] = 1
        else:
            x[j] = -1
        y[j] = matrixA[j][j] + s
    print(np.sum((np.multiply(y,y))))
    y_norm = np.sqrt(np.sum(np.multiply(y,y)))
    norm_A = y_norm/np.sqrt(length)
    return norm_A
matA = np.array([[2,0,0],[5,4,0],[3,1,6]])
norm = aprox(matA)
print(norm)
