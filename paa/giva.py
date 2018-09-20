import queue
fila=queue.PriorityQueue(maxsize=0)
def montarGrafo(caminhos):
        grafo[caminhos[0]].append([caminhos[1],caminhos[2]])
        grafo[caminhos[1]].append([caminhos[0], caminhos[2]])

def dijkstra():
    global caminho
    conti=0
    contp=0
    while fila.empty() is False:
        a = fila.get()
        aux1=a[0]
        aux2=a[1]
        aux3=a[2]
        a=[aux2,aux1,aux3]
        az=a[1]
        nx=a[2]
        for i in range(len(grafo[a[0]])):
            nivel=nx
            nivel+=1
            caminho=az
            caminho += grafo[a[0]][i][1]
            if grafoAuxImpar[grafo[a[0]][i][0]] >caminho  and nivel%2!=0:
                    grafoAuxImpar[grafo[a[0]][i][0]]=caminho
                    grafo[a[0]][i][1]=caminho
                    aux = [grafo[a[0]][i][1], grafo[a[0]][i][0], nivel]
                    fila.put(aux)
                    conti+=1
            elif grafoAuxPar[grafo[a[0]][i][0]] >caminho and  nivel%2==0:
                    grafoAuxPar[grafo[a[0]][i][0]] = caminho
                    grafo[a[0]][i][1] = caminho
                    aux = [grafo[a[0]][i][1], grafo[a[0]][i][0], nivel]
                    fila.put(aux)
                    contp+=1
        if contp>0:
            visitedp[a[0]]=1
        if conti>0:
            visitedi[a[0]]=1
        contp=0
        conti=0
casas,ruas=input().split()
casas=int(casas)
ruas=int(ruas)
visitedp=(casas+1)*[0]
visitedi=(casas+1)*[0]
fila.put([0, 1,0])
caminho=0
grafo=[]
grafoAuxImpar=(casas+1)*[100000000000000000000]
grafoAuxPar = (casas + 1) * [100000000000000000000]
grafoAuxImpar[1]=0
grafoAuxPar[1]=0
for i in range(casas+1):
    grafo.append([])
for i in range(ruas):
     caminhos=input().split()
     for i in  range(len(caminhos)):
        caminhos[i]=int(caminhos[i])
     montarGrafo(caminhos)
dijkstra()
if grafoAuxPar[casas]==100000000000000000000:
    print('-1')
else:
    print(grafoAuxPar[casas])