import random
import urllib.request
import sys
import time
start_time = time.time()
sys.setrecursionlimit(1000000)


geracoes = 100
casais_filhos = 50
tamanho_populacao = 20
porcentagem_mutacao = 7

def generateRandomConfig():
    c = list()
    for i in range(0,6):
        c.append(random.randint(0,360))
    c.append(test_config(c))
    return c

def test_config(config):
    lists = urllib.request.urlopen(
        "http://localhost:8080/antenna/simulate?phi1=" + str(config[0]) + "&theta1=" + str(config[1]) + "&phi2=" + str(
            config[2]) + "&theta2=" + str(config[3]) + "&phi3=" + str(config[4]) + "&theta3=" + str(
            config[5]) + "").read().decode().split('\n')
    return float(lists[0])


def crossover(population):
    #Normalizarei os valores de fitting quando negativo, de maneira que o primeiro seja 10.
    menor = population[0][6]
    propabilidades_normalizadas = list()
    diferenca = 0
    total =0
    if (menor < 0):
        diferenca = abs(menor)+100
    for i in range(0,tamanho_populacao):
        propabilidades_normalizadas.append(population[i][6] + diferenca)
        total+= propabilidades_normalizadas[i]
    children = list()
    for i in range(0,casais_filhos):
        selected1 = random.choices(population, weights=propabilidades_normalizadas)[0]
        selected2 = random.choices(population, weights=propabilidades_normalizadas)[0]
        criteria = random.randint(1,4)  #Em qual angulo será o ponto de crossover
        child1 = selected1.copy()  #Fim do selected2
        child2 = selected2.copy()  #Fim do selected1
        for i in range(criteria, 6):
            child1[i] = selected2[i]
            child2[i] = selected1[i]
        mutation_chance_1 = random.randint(1,100)
        mutation_chance_2 = random.randint(1,100)
        if mutation_chance_1<=porcentagem_mutacao:
            child1[random.randint(0,5)] = random.randint(0,360)
        if mutation_chance_2 <= porcentagem_mutacao:
            child2[random.randint(0, 5)] = random.randint(0, 360)
        child1[6] = test_config(child1)
        child2[6] = test_config(child2)
        children.append(child1)
        children.append(child2)
    return children


def genetic_search(population, counter):
    population.sort(key=lambda x: x[6])
    if counter==geracoes:
        return population[len(population)-1]
    population = population[len(population)-tamanho_populacao:len(population)]
    #Atualização por meio do fitting, onde o mais "fit" fica no fim.
    children = crossover(population)
    population.extend(children)
    return genetic_search(population, counter+1)

pop = list()
for i in range(tamanho_populacao):
    pop.append(generateRandomConfig())
x = genetic_search(pop,0)
print("Geracoes: ",geracoes, "| Filhos por Geração: ",casais_filhos*2,"| Tamanho da População: ",tamanho_populacao,"| Porcentagem de Mutação: ", porcentagem_mutacao,"%")
print("phi1:",x[0],"| theta1:",x[1],"| phi2:",x[2],"| theta2:",x[3],"| phi3:",x[4],"| theta3:",x[5])
print("Ganho: ",x[6])

print("--- %s seconds ---" % (time.time() - start_time))