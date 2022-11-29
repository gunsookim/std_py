def cal_rref(m):
    mat = [list(map(int, item[:])) for item in m]
    # 행렬 정렬
    mat.sort(key=lambda x: abs(x[0]), reverse=True)
    rref = [item[:] for item in mat]
    idx_r = len(mat)
    idx_c = len(mat[0])
    for r in range(idx_r):
        for c in range(idx_c - 1):
            if mat[r][c] != 0:
                for j in range(r+1, idx_r):
                    a1 = [mat[r][c] * mat[j][i] for i in range(idx_c)]
                    rref[j][:] = a1
                    show_mat(rref, j+1, j+1, mat[r][c], 1)
                    b1 = [mat[j][c] * mat[r][i] for i in range(idx_c)]
                    ero = [ai - bi for ai, bi in zip(a1, b1)]
                    rref[j][:] = ero
                    show_mat(rref, j+1, r+1, mat[j][c], 2)
                    mat[j][:] = ero
                for rj in range(r):
                    a2 = [mat[r][c] * mat[rj][i] for i in range(idx_c)]
                    rref[rj][:] = a2
                    show_mat(rref, rj+1, rj+1, mat[r][c], 1)
                    b2 = [mat[rj][c] * mat[r][i] for i in range(idx_c)]
                    ero = [ai - bi for ai, bi in zip(a2, b2)]
                    rref[rj][:] = ero
                    show_mat(rref, rj+1, r+1, mat[rj][c], 2)
                    mat[rj][:] = ero
                break
    for r in range(idx_r):
        for c in range(idx_c - 1):
            if mat[r][c] != 0:
                ero = [mat[r][i] / mat[r][c] if mat[r][i] else 0 for i in range(idx_c)]
                rref[r][:] = ero
                show_mat(rref, r+1, r+1, mat[r][c], 3)
                mat[r][:] = ero
                break
    return mat
    # mat과 크기가 같은 단위행렬 생성


def show_mat(em, r1, r2, mul, check):
    if check == 1:
        print(f"ERO 적용: ({mul})R{r1} -> R{r1}")
    elif check == 2:
        print(f"ERO 적용: (R{r1} - ({mul})R{r2}) -> R{r1}")
    elif check == 3:
        print(f"ERO 적용: R{r1}/({mul}) -> R{r1}")
    elif check == 0:
        print("RREF 결과")
    for i in range(len(em)):            # 세로 크기
        for j in range(len(em[i])-1):     # 가로 크기
            print("%-10f" % round(em[i][j], 3), end=' ')
        print("| %10f" % round(em[i][-1], 3))
    print()


if __name__ == '__main__':
    dic = {'y': True, 'yes': True, 'n': False, 'no': False}
    ans_repeat = True
    while ans_repeat:
        while True:
            try:
                filename = input("파일명 입력: ")
                with open(f"{filename}.txt", "rt") as f:
                    set_matrix = f.readline().split()
                    eq = set_matrix[0]
                    unk_v = set_matrix[1]
                    pos = f.tell()
                    rows = len(f.readlines())
                    f.seek(pos)
                    matrix = [list(map(str, f.readline().split())) for _ in range(rows)]
                break
            except FileNotFoundError:
                print("없는 파일입니다.")
        aug_matrix = [item[:] for item in matrix]
        unk_v = int(unk_v) + 1
        if len(matrix[0]) != unk_v:
            print("잘못된 행렬입니다.")
            continue
        print(f"Equation 수: {eq}, Unknown Vector 수: {unk_v}")
        print("소수점 5자리까지 출력합니다.")
        #   Augmented matrix 출력
        print("Augmented matrix: ")
        for i in range(rows):
            aug_matrix[i].insert(int(unk_v) - 1, '|')
        for i in aug_matrix:
            for j in i:
                print("%7s" % j, end=" ")
            print()
        print()
        aug_matrix = cal_rref(matrix)
        show_mat(aug_matrix, 0, 0, 0, 0)
        while True:
            try:
                ans_repeat = dic[input("반복여부 확인[y(yes) / n(no)]: ")]
                break
            except KeyError:
                print("다시 입력해주세요.")
