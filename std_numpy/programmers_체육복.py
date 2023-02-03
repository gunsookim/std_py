import sys

def solution(n, lost, reserve):
    answer = 0
    std = [1]*(n+2)
    ls = [1 if i in lost  else 0 for i in range(n+2)]
    rs = [1 if i in reserve else 0 for i in range(n+2)]
    p = [std[i] - ls[i] + rs[i] for i in range(n+2)]
    for i in range(1, n+1, 1):
        if p[i] > 1 and p[i-1] == 0:
            p[i] -= 1
            p[i-1] += 1
        if p[i] > 1 and p[i+1] == 0:
            p[i] -=1
            p[i+1] += 1
    answer = n - p.count(0)
    return answer

print(solution(5, [2,4], [3]))
