import sys

t = int(sys.stdin.readline())
n = [list(map(int, sys.stdin.readline().split())) for i in range(t)]
m = [[list(map(int, str(n[j][i]))) for i in range(2)] for j in range(t)]
num = []
for j in range(t):
    tmp = [[0]*7]*2
    for i in range(2):
        s = n[j][i]
        for k in range(1, 6):
            tmp[i][k] = s // (10 ** (7-k))
            s %= (10 ** (7-k))
    num.append(tmp)
print(n)
print(m)
print(num)