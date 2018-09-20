def bfs(adj_list, end):
    f = [(0,0)] # f= fila composta de pares (distance, node)
    n = len(adj_list) # Quantidade de vertices
    visited = []
    for i in range(n):
        visited.append(0)
    while len(f) != 0:
        curr = f.pop(0)
        visited[curr[1]] = 1  #Marca o atual como visitado
        if (curr[0] >= n):  # Se o caminho tiver passado do tamanho de vertices.. não tem como
            print ("-1")
            return
        for x in adj_list[curr[1]]:
            if visited[x]==0:  #Se transição não visitada
                f.append([curr[0]+1,x]) #Poe na fila
                visited[x] =1 #Marca como visitado, pois qualquer adicionar depois desse só sera um caminho mais longo
                if x == 25:
                    print()
                if x==end:  #Se já for o fim... acabou
                    print(curr[0]+1)
                    return
    print(-1)

t = int(input())
for a in range(t):
    n,m = input().split()
    n = int(n)
    m = int(m)
    adj_list = []
    #curr_list
    for b in range(0,n):
        adj_list.append([])
    for i in range(m):
        u,v = input().split()
        adj_list[int(u)-1].append(int(v)-1)
        adj_list[int(v)-1].append(int(u) - 1)
    bfs(adj_list,n-1)

