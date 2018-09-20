def busca1(lista, start, end, altura):
    if start > end:
        return "X"
    if start == end:
        if lista[start] >= altura:
            return "X"
        return lista[start]
    mid = (start + end) // 2
    if end - start == 1:
        mid += 1
    if lista[mid] >= altura:
        return busca1(lista, start, mid - 1, altura)
    if lista[mid] < altura:
        return busca1(lista, mid, end, altura)

def busca2(lista, start, end, altura):
    if end < start:
        return "X"
    if start == end:
        if (lista[start] <= altura):
            return "X"
        return lista[start]
    mid = (start+ end)//2
    if lista[mid] > altura:
        return busca2(lista,start, mid,altura)
    if (lista[mid] <= altura):
        return busca2(lista,mid+1,end,altura)


N = int(input())
macacas = input().split()
for i in range(len(macacas)):
    macacas[i] = int(macacas[i])
Q = int(input())
consultas = input().split()
for i in range(len(consultas)):
    print(busca1(macacas,0,N-1, int(consultas[i])), busca2(macacas,0,N-1, int(consultas[i])))

