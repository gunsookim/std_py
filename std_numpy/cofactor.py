import numpy as np


def det_cofactor(matrix):  # 1행전개로 구현

    det = 0  # 결과를 담을 객체
    dim = len(matrix)

    if dim == 2:  # 2차 행렬일 때는 ad-bc 수행

        det = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        return det

    else:

        for col in range(dim):
            # 원소 a 추출
            a = matrix[0][col]

            # 소행렬식 M 추출
            partial = np.delete(matrix, 0, axis=0)  # 1행전개
            partial = np.delete(partial, col, axis=1)

            M = det_cofactor(partial)  # 재귀함수

            sgn = (-1) ** (col)
            # 부호(실제 파이썬 인덱스는 0부터 시작하므로, 1행과 k열의 숫자 합은 col 변수와 동일한 홀/짝의 성질을 가짐)
            det += a * sgn * M

    return det

"""
array = ([[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]])

"""
array = ([[6., 1., 6., 4., 5],
          [4., 1., 7., 6., 5],
          [4., 8., 8., 2., 5],
          [3., 7., 2., 4., 5],
          [1., 3., 4., 2., 2]])


print(det_cofactor(array))
