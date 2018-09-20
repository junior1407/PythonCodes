from heapq import *

def dijkstra(graph, entrada, saida,n_vertices):
    pq = []
    heappush(pq,[0, entrada])
    visited ={}
    while len(pq)!=0:
        curr = heappop(pq)
        currTime = curr[0]
        u = curr[1]
        if u == saida:
            return currTime
        if u not in visited:
            visited[u] = []
        if (currTime%3) in visited[u]:
            continue
        visited[u].append(currTime%3)
        for x in graph[u]:
            v= x[0]
            w = x[1] # 1 : abre nos multiplos de 3.
                     # 0 : abre no resto.
            if ((w == 1 and currTime%3==0) or (w == 0 and currTime%3!=0)):
                heappush(pq, [currTime+1, v])
    return '*'






n_vertices, entrada, saida, n_edges = map(int, input().split())
graph = {}
for b in range(n_edges):
    u, v, c = map(int, input().split())
    if u not in graph:
        graph[u] = []
    graph[u].append([v, c])

distancia = dijkstra(graph,entrada,saida, n_vertices)

print(distancia)