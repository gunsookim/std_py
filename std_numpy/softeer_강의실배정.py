import sys

n = int(sys.stdin.readline())
time = sorted([list(map(int, sys.stdin.readline().split())) for i in range(n)], key=lambda x: (x[1],x[0]))
print(time)
ans = 0
now = 0
for i,j in time:
    if now<=i:
        ans += 1
        now = j
print(ans)