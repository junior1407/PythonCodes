import math
import urllib.request
import random


k = 3

def convert(l):
    l = l.split(',')
    l[0] = float(l[0])
    l[1] = float(l[1])
    l[2] = float(l[2])
    l[3] = float(l[3])
    return l

def getData():
    lists = urllib.request.urlopen(
        "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").read().decode().split('\n')
    lists = lists[0:150]
    lists = list(map(convert, lists))
    #lists = [l.split(',') for l in lists]
    return lists

def divideData(data, tSet, testSet):
    random.shuffle(data)
    tSet += data[0:100]
    testSet+= data[100:150]

def distance(o1, o2):
    d=0
    for i in range(4):
       d += (o1[i]-o2[i])**2
    return math.sqrt(d)

def getNeighbors(trainingSet, curr):
    distances = []
    for i in range(len(trainingSet)):
        if (trainingSet[i] != curr):
            # 2-Uplas  (elemento,  distancia)
            distances.append((trainingSet[i],distance(curr, trainingSet[i])))
    distances.sort(key=lambda x: x[1])
    return distances[0:k]

def getType(neighbors):
    possibilidades = {}
    for i in range(len(neighbors)):
        tipo = neighbors[i][0][4]
        if tipo in possibilidades:
            possibilidades[tipo]+=1
        else:
            possibilidades[tipo]=1
    sortado = sorted(possibilidades.items(), key= lambda x: x[1])
    return sortado[-1][0]
def test(trainingSet,testSet):
    acertou=0
    for a in testSet:
        if (getType(getNeighbors(trainingSet, a)) == a[4]):
            acertou +=1
    print("Acertos: ",acertou)
    print("Acurácia: ", acertou/len(testSet))
data = getData()
trainingSet = []
testSet = []
divideData(data, trainingSet, testSet)
curr = testSet[0]
test(trainingSet,testSet)


#