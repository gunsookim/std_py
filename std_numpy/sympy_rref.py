from sympy import Matrix
import numpy as np


def pivoting(a):
    cal_rref = a.rref()
    return cal_rref


if __name__ == '__main__':
    mat1 = np.array([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12]])
    mat2 = Matrix([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])
    # rref_np = pivoting(mat1)
    rref_sp = pivoting(mat2)
    print(f"RREF = {rref_sp}\n")
