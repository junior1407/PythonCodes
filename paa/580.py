import heapq

def dijkstra(start, graph, distances,destination):
    distances[start] = 0
    pq = []
    contador =0
    heapq.heappush(pq, [0, start])
    # pq.put([0, start])  # Distancia, Node
    while pq:
        # curr = pq.get()
        curr = heapq.heappop(pq)
        u = curr[1]
        dist = curr[0]
        if (dist > distances[u]):
            pass
        for x, item in graph[u].items():
            v = item[0]
            w = item[1]
            if distances[v] > distances[u] + w:
                distances[v] = distances[u] + w
                # pq.put([-distances[v], v])
                heapq.heappush(pq, [distances[v], v])
            if u == destination:
                contador+=1
            #    if v == destination:
             #       return


n_vertices, n_edges = map(int, input().split())
graph = {}
graphpar = {}
for b in range(n_edges):
    u, v, c = map(int, input().split())
    u = u - 1
    v = v - 1
    if u not in graph:
        graph[u] = []
        graphpar[u] = {}
    graph[u].append([v, c])
    if v not in graph:
        graph[v] = []
        graphpar[v] = {}
    graph[v].append([u, c])

for v1, edges1 in graph.items():
    origem = v1
    for e1 in edges1:
        destino1 = e1[0]
        peso1 = e1[1]
        for v2 in graph[destino1]:
            destino2 = v2[0]
            peso2 = v2[1]
            if destino1 != destino2 != origem:
                if destino2 not in graphpar[origem]:
                    graphpar[origem][destino2] = [destino2, peso1 + peso2]
                else:
                    if graphpar[origem][destino2][1] > peso1 + peso2:
                        graphpar[origem][destino2][1] = peso1 + peso2

distances = []
for b in range(n_vertices):
    distances.append(1048576)

dijkstra(0, graphpar, distances,n_vertices - 1)
if distances[n_vertices - 1] == 1048576:
    print("-1")
else:
    print(distances[n_vertices - 1])
