def valid(x,y):
    if x<1 or x>5 or y<1 or y>5:
        return False
    else:
        return True


def dfs(x,y, arr, visit, a):
    cnt = 0
    if valid(x,y) and visit[y][x] != 'C':
        if arr[y][x] == 'P':
            if arr[y][x-1] == 'P' or arr[y][x+1] == 'P' or arr[y-1][x] == 'P' or arr[y+1][x] == 'P':
                return 0
        if arr[y][x] == 'O':
            if arr[y][x-1] == 'P': cnt += 1
            if arr[y][x+1] == 'P': cnt += 1
            if arr[y-1][x] == 'P': cnt += 1
            if arr[y+1][x] == 'P': cnt += 1
            if cnt > 1: return 0
        visit[y][x] = 'C'
        a = dfs(x+1, y, arr, visit, a)
        a = dfs(x-1, y, arr, visit, a)
        a = dfs(x, y+1, arr, visit, a)
        a = dfs(x, y-1, arr, visit, a)
    return a


def solution(places):
    answer = []
    for i in places:
        x = 'XXXXX'
        i.insert(0, x)
        i.append(x)
        arr = [list('X' + j + 'X') for j in i]
        visit = [[0]*7 for j in range(7)]
        answer.append(dfs(1,1,arr,visit, 1))
    return answer


solution([["POOOP",
           "OXXOX",
           "OPXPX",
           "OOXOX",
           "POXXP"],
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])