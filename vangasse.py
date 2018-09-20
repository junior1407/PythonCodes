def acha_corte(c, menor, maior, altura):
    meio = (menor + maior) / 2
    soma = 0
    for i in range(len(c)):
        if c[i] - meio > 0:
            soma = soma + c[i] - meio
    if soma - altura <= 0.001 and soma - altura >= -0.001:
        print("{0:.4f}".format(meio))
        return
    if soma - altura >= 0.001:
        return acha_corte(c, meio, maior, altura)
    if soma - altura <= -0.001:
        return acha_corte(c, menor, meio, altura)


na = input().split()
n = int(na[0])
a = int(na[1])

while n != 0 and a != 0:
    str_comprimentos = input().split()
    maior = 0
    soma_sorriso = 0
    for i in range(len(str_comprimentos)):
        str_comprimentos[i] = int(str_comprimentos[i])
        soma_sorriso = soma_sorriso + str_comprimentos[i]
        if str_comprimentos[i] > maior:
            maior = str_comprimentos[i]
    if soma_sorriso == a:
        print(":D")
    elif soma_sorriso < a:
        print("-.-")
    else:
        acha_corte(str_comprimentos, 0, float(maior), a)
    na = input().split()
    n = int(na[0])
    a = int(na[1])