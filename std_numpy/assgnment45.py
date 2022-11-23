def cal_rref(m):
    return m


if __name__ == '__main__':
    dic = {'y': True, 'yes': True, 'n': False, 'no': False}
    ans_repeat = True
    while ans_repeat:
        filename = input("파일명 입력: ")
        with open(f"{filename}.txt", "rt") as f:
            set_matrix = f.readline().split()
            eq = set_matrix[0]
            unk_v = set_matrix[1]
            pos = f.tell()
            rows = len(f.readlines())
            f.seek(pos)
            matrix = [list(map(str, f.readline().split())) for _ in range(rows)]

            #Augmented matrix 출력
            for i in range(rows):
                matrix[i].insert(int(unk_v) - 1, '|')
            for i in matrix:
                for j in i:
                    print(j, end=" ")
                print()

        ans_repeat = dic[input("반복여부 확인[y(yes) / n(no)]: ")]
"""
        while True:
            ans_repeat = input("반복여부 확인[y(yes) / n(no)]: ")
            if ans_repeat in dic:
                ans_repeat = dic[ans_repeat]
                break
            else:
                print("다시 입력해주세요.")"""

