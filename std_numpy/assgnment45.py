def cal_rref(m):
    idx_row = list(range(len(m)))
    idx_col = len(m[0]) - 1
    m_pivot = [list(map(int, item[:])) for item in m]
    ero = []
    #   행렬 정렬
    print(idx_row)
    m_pivot.sort(key=lambda x: abs(x[0]), reverse=True)
    """for c in range(idx_col):
        nz_row = [r for r in idx_row if m_pivot[r][c] != 0]
        if nz_row:
            pivot = nz_row[0]
            idx_row.remove(pivot)
            ero.append(m_pivot[pivot])
            for r in nz_row:
                if r is not pivot:"""
    print(f"ERO: {m_pivot}")
    # for row in range(len(idx_row)):


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
                    print(f"Equation 수: {eq}, Unknown Vector 수: {unk_v}")
                    pos = f.tell()
                    rows = len(f.readlines())
                    f.seek(pos)
                    matrix = [list(map(str, f.readline().split())) for _ in range(rows)]
                break
            except FileNotFoundError:
                print("없는 파일입니다.")
        aug_matrix = [item[:] for item in matrix]
        #   Augmented matrix 출력
        for i in range(rows):
            aug_matrix[i].insert(int(unk_v) - 1, '|')
        for i in aug_matrix:
            for j in i:
                print(j, end=" ")
            print()
        cal_rref(matrix)
        while True:
            try:
                ans_repeat = dic[input("반복여부 확인[y(yes) / n(no)]: ")]
                break
            except KeyError:
                print("다시 입력해주세요.")
