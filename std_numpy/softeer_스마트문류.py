import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(sys.stdin.readline().replace('\n', ''))
print(arr)
cnt = 0
for i in range(n):
    if arr[i] == 'P':
        for j in range(-k+i, k+i+1):
            if j<0 or j>=n:
                continue
            elif arr[j]=='H':
                arr[j] = 0
                cnt += 1
                break
print(cnt)