import numpy as np
from ainv_aprox import inv_aprox
from a2_aprox import aprox

matA = np.array([[2,0,0],[5,4,0],[3,1,6]])
inv_norm = inv_aprox(matA)
norm = aprox(matA)

condition_number = norm*inv_norm
print(condition_number)
