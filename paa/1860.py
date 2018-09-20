def bfs(capacidade, dividas, adj_list, atual, origem):
    distancia_atual = 0
    cofre_atual= divida[atual]
    for i in range(len(adj_list[atual])):
        destino, peso = adj_list[atual][i]
        if (destino!= origem):
            ret_ouro, ret_dist = bfs(capacidade, dividas, adj_list,destino, atual)
            distancia_atual+=ret_dist
            cofre_atual+=ret_ouro
            idas = ret_ouro // capacidade
            if ret_ouro % capacidade!=0:
                idas+=1
            distancia_atual+= 2 * idas * peso
    return(cofre_atual,distancia_atual)


n,c = map(int,input().split())
divida = list(map(int, input().split()))
divida[0] = 0
adj_list = []
for a in range(n):
    adj_list.append([])
for a in range(n-1):
    u,v,w = map(int,input().split())
    adj_list[u-1].append([v-1,w])
    adj_list[v - 1].append([u - 1, w])
print(bfs(c,divida,adj_list,0,0)[1])
