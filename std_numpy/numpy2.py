import numpy as np


def calculater(m1, m2, c):  # 행렬 계산 함수
    result = {'+': m1 + m2, '-': m1 - m2, '*': m1 * m2, '/': m1 / m2, '@': m1 @ m2}    # 딕셔너리를 이용해 입력에 따라 다른 계산 실행
    # *은 요소 간의 곱을 계산, @은 행렬 곱을 계산
    return result[c]


if __name__ == '__main__':
    mat1 = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])
    mat2 = np.array([[10, 11, 12],
                     [13, 14, 15],
                     [16, 17, 18]])
    cal = input("계산 입력: ")
    print(calculater(mat1, mat2, cal))
