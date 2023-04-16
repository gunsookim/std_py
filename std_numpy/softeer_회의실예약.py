import sys

n,m = map(int, sys.stdin.readline().split())
room = sorted([sys.stdin.readline().replace('\n', '') for _ in range(n)])
booked = [['09' if i==0 else str(i+9) for i in range(9)] for _ in range(n)]

for _ in range(m):
    name, start, end = list(sys.stdin.readline().split())
    for i in range(int(start)-9, int(end)-9):
        booked[room.index(name)][i] = ' '
x = [''.join(booked[i]).split() for i in range(n)]
for r in range(n):
    cnt = len(x[r])
    print(f"Room {room[r]}:")
    if cnt == 0 :
        print("Not available")
    else:
        print(f"{cnt} available:")
        for i in range(cnt):
            start = str(int(x[r][i][0:2])).zfill(2)
            end = str(int(x[r][i][-2:])+1).zfill(2)
            print(f"{start}-{end}")
    if r < n-1 :
        print("-----")