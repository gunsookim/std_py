import sys

n,m = list(map(int, sys.stdin.readline().split()))
stand = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
test = [list(map(int, sys.stdin.readline().split())) for r in range(m)]
s1 = sum([[stand[j][1] for i in range(stand[j][0])] for j in range(len(stand))], [])
s2 = sum([[test[j][1] for i in range(test[j][0])] for j in range(len(test))], [])
s3 = max([s2[a] - s1[a] for a in range(len(s1))])
if s3 <= 0:
    s3 = 0
print(s3)
