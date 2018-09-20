from heapq import *
from math import sqrt


def dfs(graph,n_arvores, u):
    global visited_counter
    global visited
    if visited[u] ==1:
        return
    visited[u] =1
    visited_counter+=1
    if visited_counter==n_arvores:
        return
    for v in graph[u]:
            if visited[v]==0 and visited_counter!=n_arvores:
                dfs(graph, n_arvores, v)


n_arvores, alcance = map(int, input().split())
contador = 0
arvores = []

for i in range(n_arvores):
    x, y= map(int,input().split())
    arvores.append([x,y])
graph= {}
for i in range(n_arvores):
    for j in range(n_arvores):
        if i!=j:
            if (i not in graph):
                graph[i] = []
            if j not in graph:
                graph[j]=[]
            if sqrt((arvores[i][0] - arvores[j][0]) * (arvores[i][0] - arvores[j][0]) +
                    (arvores[i][1] - arvores[j][1]) * (arvores[i][1] - arvores[j][1])) <= alcance:
                graph[i].append(j)
                graph[j].append(i)



visited = [0] * n_arvores
visited_counter = 0
dfs(graph,n_arvores,0)
if visited_counter == n_arvores:
    print('S')
else:
    print('N')







