
def busca_comeco(lista, referencia,start, end):
    mid = (start+end)//2
    if start>end:
        return end
    if (end-start==1):
        mid+=1
    if (start==end):
        return start
    if (lista[mid] > referencia):
        return busca_comeco(lista,referencia,start,mid-1)
    if lista[mid] <= referencia:
        return busca_comeco(lista,referencia,mid+1,end)



def busca(lista, start, end, altura):
    mid = (start+end)/2
    soma=0
    #comeco = busca_comeco(lista, mid, 0, len(lista)-1)
    for i in range(busca_comeco(lista, mid, 0, len(lista)-1),len(lista)):
        if (lista[i]- mid)>0:
            soma+=lista[i]- mid
    if abs(soma-altura) <=0.001:
        return mid
    if soma>altura:
        return busca(lista, mid+1, end, altura)
    if soma<altura:
        return busca(lista, start,mid-1,altura)


n, a = input().split()
n = int(n)
a = int(a)
while n!=0  and a!= 0:
    lista = input().split()
    maior =-1
    for i in range(len(lista)):
        lista[i] =  int(lista[i])
        if lista[i]>maior:
            maior = lista[i]
    lista.sort()
    soma= sum(lista)
    #maior = max(lista)
    if soma==a:
        print(":D")
    elif soma<a:
        print("-.-")
    else:
        print("{:.4f}".format(busca(lista, 0, maior, a)))
    n, a = input().split()
    n = int(n)
    a = int(a)