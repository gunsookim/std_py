import sys
from collections import deque

def bfs():
    que = deque([[0,0]])
    visit[0][0] = 1
    while que:
        y, x = que.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=nx<m and 0<=ny<n:
                if arr[ny][nx] == 1:
                    visit[ny][nx] += 1
                elif visit[ny][nx] == 0:
                    que.append([ny, nx])
                    visit[ny][nx] = 1
    for y in range(n):
        for x in range(m):
            if visit[y][x] >= 2:
                arr[y][x] = 0

n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split()))for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
time = 0
while True:
    if arr.count([0]*m) == n:
        break
    visit = [[0]*m for _ in range(n)]
    bfs()
    time += 1
print(time)
