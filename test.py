import heapq

INF = float('inf')
n = 4
g = {
    0: [(1,2), (3,5)],
    1: [(2,4), (3,1)],
    2: [(2,1)],
    3: []
}

dist = [INF]*n
dist[0] = 0
prev = [None]*n

pq = [(0,0)]  # (расстояние, вершина)

while pq:
    d, u = heapq.heappop(pq)
    if d != dist[u]:
        continue  # устаревшее значение
    for v,w in g[u]:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            prev[v] = u
            heapq.heappush(pq, (dist[v], v))
    print(f"pop ({d},{u}), heap={pq}, dist={dist}")
