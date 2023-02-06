import sys

n = int(sys.stdin.readline())
score = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
score.append([score[0][i] + score[1][i] + score[2][i] for i in range(n)])
for i in range(4):
    rank = [print(sorted(score[i], reverse = True).index(x)+1, end=' ') for x in score[i]]
    print()
    
"""
n = int(sys.stdin.readline())
tot = [0]*n
for i in range(3):
    score = list(map(int, sys.stdin.readline().split()))
    tot = [tot[j]+score[j] for j in range(n)]
    rank = [print(sorted(score, reverse = True).index(x)+1, end=' ')for x in score]
    print()
[print(sorted(tot, reverse = True).index(x)+1, end=' ' )for x in tot]
"""
"""
n = int(sys.stdin.readline())
tot = [0]*n
for i in range(3):
    rank = [1]*n
    score = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        tot[j] += score[j]
        for k in range(n):
            if score[j] > score[k]:
                rank[k] += 1
    print(rank)
rank = [1]*n
for x in range(n):
    for y in range(n):
        if tot[x] > tot[y]:
            rank[y] += 1
print(rank)
"""