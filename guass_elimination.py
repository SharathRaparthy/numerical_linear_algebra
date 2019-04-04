import numpy as np

class GuassElimination(object):
    """docstring forGuassElimination."""
    def __init__(self, input_matrix, b, partial_pivoting, epsilon = 1e-4):
        super(GuassElimination, self).__init__()
        self.input_matrix = input_matrix
        self.partial_pivoting = partial_pivoting
        self.epsilon = epsilon
        self.b = b
    def guass_elim(self):
        length = len(self.input_matrix[0])
        # matrix = self.input_matrix
        matrix = np.concatenate((self.input_matrix, self.b), axis = 1)

        for i in range(length):
            #check if pivotal element is zero or not
            if matrix[i][i] == 0:

                tmp = matrix[i].copy()
                matrix[i] = matrix[i+1]
                matrix[i+1] = tmp
            mul_fac = [matrix[j][i]/matrix[i][i] for j in range(i+1, length)]
            for idx,k in enumerate(range(i+1, length)):
                matrix[k][:] = matrix[k][:] - mul_fac[idx]*matrix[i][:]
        return matrix

input_array = np.array([[1,-1,2,-1],[2,-2,3,-3],[1,1,1,0],[1,-1,4,3]])
b = np.array([[-8],[-20],[-2],[4]])

guass_elimination = GuassElimination(input_array, b, partial_pivoting = False, epsilon =1e-4)
gaussian_matrix = guass_elimination.guass_elim()
print(gaussian_matrix)
leng = len(gaussian_matrix[0])
coefficient_matrix = np.delete(gaussian_matrix, leng-1, 1)
b_matrix = gaussian_matrix[:, leng - 1]
x = np.matmul(np.linalg.inv(coefficient_matrix),b_matrix)
print(x)
