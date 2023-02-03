import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
finish_a = arr[0][0]
finish_b = arr[0][1]
for i in range(1, len(arr)):
    tmp_a = finish_a
    tmp_b = finish_b
    finish_a = min(tmp_a, tmp_b + arr[i-1][3]) + arr[i][0]
    finish_b = min(tmp_b, tmp_a + arr[i-1][2]) + arr[i][1]
    print(finish_a, finish_b)