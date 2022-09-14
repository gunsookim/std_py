def calculate():
    with open("Input.txt", "rt") as f:
        num_m = int(f.readline())   # 행렬을 저장할 리스트의 개수를 저장합니다. readline()를 통해 한줄씩 처리합니다.
        set_m1 = list(map(str, f.readline().split()))   # 행렬 A의 정보(이름, 행, 열)를 리스트로 저장합니다.
        m1 = [list(map(int, f.readline().split())) for _ in range(int(set_m1[1]))]  # 행렬의 요소를 2차원 리스트로 저장합니다.
        f.readline()    # 빈 줄을 통해 행렬을 구분합니다.
        set_m2 = list(map(str, f.readline().split()))   # 행렬 B의 정보(이름, 행, 열)를 리스트로 저장합니다.
        m2 = [list(map(int, f.readline().split())) for _ in range(int(set_m2[1]))]  # 행렬의 요소를 2차원 리스트로 저장합니다.
        with open("Output.txt", "wt") as f_out:     # 결과를 Output.txt에 저장하며 모드는 wt입니다.
            if int(set_m1[1]) != int(set_m2[1]) or int(set_m1[2]) != int(set_m2[2]):    # 두 행렬의 차원이 다른 경우 +계산 불가
                f_out.write(f"+ 계산 불가")
            else:   # 두 행렬의 차원이 같으므로 +계산을 한 뒤, 파일에 저장 합니다.
                result = [[m1[i][j] + m2[i][j] for j in range(int(set_m1[2]))] for i in range(int(set_m1[1]))]
                for i in range(int(set_m1[1])):
                    for j in range(int(set_m1[2])):
                        f_out.write(str(result[i][j]) + ' ')
                    f_out.write('\n')


if __name__ == '__main__':
    calculate()
