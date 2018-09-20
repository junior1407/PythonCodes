def busca(tiras, area, begin, end, n):
    area_soma = 0
    middle = (begin + end) / 2
    ind = 0

    for i in range(n):
        if ((tiras[i]) > middle):
            area_soma += (tiras[i]) - middle

    if (abs(area_soma - area) <= 0.001):
        return middle

    elif (area > area_soma):
        return busca(tiras, area, begin, middle - 1, n)

    else:
        return busca(tiras, area, middle + 1, end, n)


n, a = input().split(" ")
a = int(a)
n = int(n)

while (a != 0 and n != 0):
    tirasStr = input().split(" ")

    tirasInt = []

    for i in range(n):
        tirasInt.append(int(tirasStr[i]))

    areaTotal = sum(tirasInt)
    maior = max(tirasInt)

    tirasInt.sort()

    if (areaTotal < a):
        print("-.-")

    elif (areaTotal == a):
        print(":D")

    else:
        print("{:.4f}".format(busca(tirasInt, a, 0, maior, n)))

    n, a = input().split(" ")
    a = int(a)
    n = int(n)