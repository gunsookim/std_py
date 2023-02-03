import sys

k, p, n = map(int, sys.stdin.readline().split())

def cal(p, n):
    if n == 1:
        return p
    x = cal(p, n//2)
    if n%2 == 0:
        return (x % 1000000007) * (x % 1000000007) % 1000000007
    else:
        return (x % 1000000007) * (x % 1000000007) * (p % 1000000007) % 1000000007
k *= cal(p, n*10)
print(k)

""" # 재귀함수 사용전
for i in range(10*n):
    k = ((p % 1000000007) * (k % 1000000007)) % 1000000007
print(k)
"""