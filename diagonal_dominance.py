import numpy as np

class DiagonalDominance(object):
    """docstring forDiagonalDominance."""
    def __init__(self, input_matrix):
        super(DiagonalDominance, self).__init__()
        self.input_matrix = input_matrix
    def is_square(self,input_matrix):
        height, width = self.input_matrix.shape
        if height == width:
            print("The given matrix is a square matrix")
            is_true = True
        else:
            print("The given matrix is not a diagonal matrix")
            is_true = False
        return is_true
    def diagonal_dominance(self):
        delta = []
        summation = []
        is_tr = self.is_square(self.input_matrix)
        if is_tr:
            diag = [self.input_matrix[i][i] for i in range(len(self.input_matrix[0]))]
            for i in range(len(self.input_matrix[0])):
                row_sum = 0
                for j in range(len(self.input_matrix[0])):
                    if i != j:
                        row_sum = row_sum + np.abs(self.input_matrix[i][j])
                if row_sum > np.abs(diag[i]):
                    print("The matrix is not diagonally dominant")
                    break;
                summation.append(row_sum)
                delta_ = np.abs(diag[i]) - row_sum
                delta.append(delta_)
        return delta
    def infinity_norm(self):
        norms = np.sum(np.abs(self.input_matrix), axis=1)
        return np.max(norms)
    def conditional_num(self):
        infinity_norm = self.infinity_norm()
        delta = self.diagonal_dominance()
        delta_min = min(delta)
        print("The matrix is diagonally dominant")
        print(f'The conditional number is :{infinity_norm/delta_min}')
        return infinity_norm/delta_min

matrix_input = np.array([[10,1,5],[2,8,5],[3,1,18]])
diagonal_dom = DiagonalDominance(matrix_input)
delt = diagonal_dom.conditional_num()
