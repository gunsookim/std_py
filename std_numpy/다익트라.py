import heapq


def solution(n, road, k):
    graph = [[] for _ in range(n+1)]

    for i in road:
        graph[i[0]].append((i[1],i[2]))
        graph[i[1]].append((i[0],i[2]))

    dist = [10**9] * (n+1)


    def dijkstra(start):
        dist[start] = 0
        q = list()
        heapq.heappush(q, [0,start])

        while q:
            curdist, now = heapq.heappop(q)#0, 1
            if dist[now] < curdist:
                continue
            for i in graph[now]:
                cost = curdist + i[1]
                if cost < dist[i[0]]:
                    dist[i[0]] = cost
                    heapq.heappush(q,[cost,i[0]])

    dijkstra(1)
    cnt =0
    for i in dist:
        if i <=k:
            cnt+=1
    return cnt