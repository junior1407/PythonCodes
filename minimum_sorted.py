def find_menor(lista, left, right, cabeca):
    if(left == right):
        return lista[left]
    mid = (left+right)//2
    if(lista[mid] >= cabeca):
        return find_menor(lista, mid+1, right, cabeca)
    else:
        return find_menor(lista, left, mid, cabeca)



cases = int(input())
n_elmements = int(input())
lista = input().split()
for i in range(len(lista)):
    lista[i] = int(lista[i])
print(find_menor(lista, 1, n_elmements-1, lista[0]))

