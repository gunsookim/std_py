
if __name__ == '__main__':
    filename = input("파일명 입력: ")

    with open(f"{filename}.txt", "rt") as f:
        row = len(f.readlines())
        matrix = [list(map(int, f.readline().split())) for _ in range(row)]

    print(matrix)
