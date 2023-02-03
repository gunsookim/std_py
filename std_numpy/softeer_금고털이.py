import sys

w, n = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
a.sort(key=lambda x: -x[1])
tmp = 0
for i in range(n):
    if a[i][0] < w:
        tmp += a[i][0]*a[i][1]
        w -= a[i][0]
    else:
        tmp += w*a[i][1]
        break
print(w,n)
print(a)
print(tmp)
