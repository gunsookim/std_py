import sys
from itertools import permutations

n,m,k = map(int, sys.stdin.readline().split())
w = list(map(int, sys.stdin.readline().split()))
cnt = 0
ans = []
arr = list(permutations(w,n))
for x in arr:
    tot = 0
    cnt = 0
    for i in range(k):
        basket = 0
        while True:
            basket += x[cnt]
            cnt = (cnt+1)%n
            if basket + x[cnt] > m:
                break
        tot += basket
    ans.append(tot)
print(min(ans))