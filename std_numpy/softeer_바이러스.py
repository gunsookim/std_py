import sys

n = list(map(int, sys.stdin.readline().split()))
a=1
while n[2]:
    if n[2] & 1:
        a = (a*n[1])%1000000007
    n[1] = (n[1] ** 2)%1000000007
    n[2] //= 2
a = (a*n[0])%1000000007
print(a)
