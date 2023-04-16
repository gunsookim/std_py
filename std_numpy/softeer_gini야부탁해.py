import sys

def diffusion_rain(): # 소나기 확산 함수
    tmp = rain[:]
    for a in tmp:
        for i in range(4):
            nx = a[0]+dx[i]
            ny = a[1]+dy[i]
            if 0<=nx<c and 0<=ny<r:
                if arr[ny][nx]=='.':
                    arr[ny][nx] = '*'
                    rain.append([nx,ny])
                    #rain.pop()

def bfs(): # 이동 함수
    for a, b in que:
        que.pop()
        for i in range(4):
            nx = a+dx[i]
            ny = b+dy[i]
            if 0<=nx<c and 0<=ny<r:
                if end == [nx,ny]:
                    start[0], start[1] = nx,ny
                if visit[ny][nx] == 0 and arr[ny][nx]=='.':
                    que.append([nx, ny])
                    visit[ny][nx] = 1


r,c = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().replace('\n', ''))for _ in range(r)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
time = 0
rain = []
visit=[[0]*c]*r
start = [0,0]
end = [0,0]

for y in range(r):
    for x in range(c):
        if arr[y][x] == 'H':
            start[0], start[1] = x,y
        if arr[y][x] == 'W':
            end[0], end[1] = x,y
        if arr[y][x] == '*':
            rain.append([x,y])

que = [start[:]]
while True:
    if start == end:
        print(time)
        break
    if len(que) == 0:
        print("FAIL")
        break
    diffusion_rain()
    bfs()
    time += 1