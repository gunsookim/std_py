def load_matrix(r):
    with open("Input.txt", "rt") as f_in:
        matrix = [list(map(int, f_in.readline().split())) for _ in range(r)]
        for i in range(r):
            if r != len(matrix[i]):
                print("Non-square matrix")
                return None
        print("계산 가능")
        return cal_sub(matrix)


def cal_sub(m):
    det = 0
    val = len(m)
    if val == 2:
        det = m[0][0] * m[1][1] - m[1][0] * m[0][1]
        return det
    else:
        for col in range(val):
            a = m[0][col]
            sub_mat = [[m[i+1][j] for j in range(val) if j != col] for i in range(val-1)]
            mat1 = cal_sub(sub_mat)
            sgn = (-1)**col
            det += a*sgn*mat1
    return det


if __name__ == '__main__':
    with open("Input.txt", "rt") as f:
        row = len(f.readlines())
    d = load_matrix(row)
    with open("Output.txt", "wt") as f_out:
        f_out.write(str(d))
