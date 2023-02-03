import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
tmp = [1]*n
for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            tmp[i] = max(tmp[i], tmp[j]+1)
print(tmp)