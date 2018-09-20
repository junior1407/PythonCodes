import heapq
def dijkstra(start, graph, distances,destination):
    distances[start] = [0,1048576]
    pq = []
    heapq.heappush(pq, [0, start])
    while pq:
        curr = heapq.heappop(pq)
        u = curr[1]

        dist = curr[0]

        for item in graph[u]:
            v = item[0]
            w = item[1]
            if distances[v][0] > distances[u][1] + w:
                distances[v][0] = distances[u][1] + w
                # pq.put([-distances[v], v])
                heapq.heappush(pq, [distances[v][0], v])
            if distances[v][1] > distances[u][0] + w:
                distances[v][1] = distances[u][0] + w
                # pq.put([-distances[v], v])
                heapq.heappush(pq, [distances[v][1], v])


n_vertices, n_edges = map(int, input().split())
graph = {}
for b in range(n_edges):
    u, v, c = map(int, input().split())
    u = u - 1
    v = v - 1
    if u not in graph:
        graph[u] = []
    graph[u].append([v, c])
    if v not in graph:
        graph[v] = []
    graph[v].append([u, c])


distances = []
for b in range(n_vertices):
    distances.append([1048576,1048576])

dijkstra(0, graph, distances,n_vertices - 1)
if distances[n_vertices - 1][0] == 1048576:
    print("-1")
else:
    print(distances[n_vertices - 1][0])
