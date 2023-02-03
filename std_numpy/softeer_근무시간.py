import sys

work = [sys.stdin.readline().replace(':','').split() for i in range(5)]
time = [(((int(work[i][1])//100)*60 + int(work[i][1])%100) -
         ((int(work[i][0])//100)*60 +int(work[i][0])%100)) for i in range(5)]
print(int(sum(time)))
