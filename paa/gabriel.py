from heapq import *
def bfs(graph, entrada, saida):
    tempo = 0
    tempoTotal = 0
    status = [[] for k in range(len(graph))]
    pq = []
    dist = -1
    heappush(pq, [0, entrada])
    while (len(pq) != 0):
        v = heappop(pq)
        e = v[1]
        tempoTotal = v[0]
        tempo = tempoTotal % 3
        print(status[e])
        print(e," - ",status[e],"and",tempo)
        if (tempo in status[e]):
            continue
        status[e].append(tempo)
        if (e == saida):
            dist = tempoTotal
            break
        for i in range(len(graph[e])):
            v = graph[e][i]
            if (v[1] == 0):
                if (tempo % 3 != 0):
                    heappush(pq, [tempoTotal + 1, v[0]])
            elif (v[1] == 1):
                if (tempo % 3 == 0):
                    heappush(pq, [tempoTotal + 1, v[0]])
    return dist
# main
'''
Temporiza??o:
    t = 0 => semafaro fecha nos multiplos de 3
    t = 1 => semafaro abre nos multiplos de 3
'''
rotatorias, entrada, saida, ruas = map(int, input().split())
graph = [[] for k in range(rotatorias)]
for i in range(ruas):
    inicio, fim, t = map(int, input().split())
    graph[inicio].append([fim, t])

dist = bfs(graph, entrada, saida)
if (dist == -1):
    print("*")
else:
    print(dist)
