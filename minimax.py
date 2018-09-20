counter = 0
machine = 0

def evaluate(tabuleiro):
    diagP = [0, 0]
    diagS = [0, 0]
    linha = [[0, 0], [0, 0], [0, 0]]
    coluna = [[0, 0], [0, 0], [0, 0]]
    flag = False
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == -1:
                flag=True
            else:
                if (i == j):  # caso Diagonal Principal
                    diagP[tabuleiro[i][j]] += 1
                if (i + j == 2):  # Caso diagonal Secundaria
                    diagS[tabuleiro[i][j]] += 1
                if (tabuleiro[i][j]!=-1):
                    linha[i][tabuleiro[i][j]] += 1
                    coluna[j][tabuleiro[i][j]] += 1
    if (linha[0][0] == 3 or linha[1][0] == 3 or linha[2][0] == 3 or coluna[0][0] == 3 or coluna[1][0] == 3 or coluna[2][
        0] == 3 or diagP[0] == 3 or diagS[0] == 3):
        return 0
    if (linha[0][1] == 3 or linha[1][1] == 3 or linha[2][1] == 3 or coluna[0][1] == 3 or coluna[1][1] == 3 or coluna[2][
        1] == 3 or diagP[1] == 3 or diagS[1] == 3):
        return 1
    if not flag:
        return -1
    return None


def copyTabuleiro(tabuleiro):
    new = []
    new.append([tabuleiro[0][0], tabuleiro[0][1], tabuleiro[0][2]])
    new.append([tabuleiro[1][0], tabuleiro[1][1], tabuleiro[1][2]])
    new.append([tabuleiro[2][0], tabuleiro[2][1], tabuleiro[2][2]])
    return new


def generateChildren(node):
    if (node.evaluation != None):
        return []
    global counter
    children = []
    for i in range(3):
        for j in range(3):
            if (node.estadoAtual[i][j] == -1):
                counter += 1
                # new = copyTabuleiro(node.estadoAtual.tabuleiro)
                new = [row[:] for row in node.estadoAtual]
                new[i][j] = node.vez
                if (counter == 986000):
                    print()
                children.append(Node(new, node, 1 - node.mini, 1 - node.vez))
    return children


class Node:
    def __init__(self, estadoAtual, anterior, mini, vez):
        self.evaluation = None
        self.nodeAnterior = anterior
        if anterior is None:
            self.custo = 0
        else:
            self.custo = self.nodeAnterior.custo + 1
        self.estadoAtual = estadoAtual
        if (self.custo >= 0):
            self.winner = evaluate(estadoAtual)
        else:
            self.winner = None
        self.mini = mini  # 1 - min, 0 - max
        self.vez = vez  # Vez do PROXIMO
        if self.winner == None:
            self.children = generateChildren(self)
        else:
            self.children = []
        if self.winner != None:
            if (self.winner == -1):
                self.evaluation=0
            elif (self.winner == machine):
                self.evaluation=1
            else:
                self.evaluation=-1
        if self.winner is None and self.nodeAnterior is not None:
            maximo=self.children[0].evaluation
            minimo= self.children[0].evaluation
            for i in range(len(self.children)):
                if (self.children[i].evaluation > maximo):
                    maximo=self.children[i].evaluation
                if (self.children[i].evaluation < minimo):
                    minimo =self.children[i].evaluation
            if (self.mini==1):
                self.evaluation= minimo
            if self.mini==0:
                self.evaluation = maximo
                    #percorre os filhos pra dizer.



def printTabuleiro(tabuleiro):
    for i in range(3):
        a = str(tabuleiro[i][0])
        if (tabuleiro[i][0] == -1):
            a = "_"
        b = str(tabuleiro[i][1])
        if (tabuleiro[i][1] == -1):
            b = "_"
        c = str(tabuleiro[i][2])
        if (tabuleiro[i][2] == -1):
            c = "_"
        print(a,b,c)

tabuleiro = []
tabuleiro.append([-1, -1,-1])
tabuleiro.append([-1, -1,-1])
tabuleiro.append([-1, -1,-1])
print("Voce será o 1")
root = None
while True:
    print("Sua vez 1")
    if (root==None):
        printTabuleiro(tabuleiro)
    else:
        printTabuleiro(root.estadoAtual)
    print("Onde deseja jogar?  linha coluna separados por espaco")
    l,c = input().split()
    if root is None:
        tabuleiro[int(l)][int(c)]=1
    else:
        for i in range(len(root.children)):
            if root.children[i].estadoAtual[int(l)][int(c)] == 1:
                root= root.children[i]
                break
    if root is not None and (root.winner is not None):
        break
    print("Vez da Máquina")
    if root is None:
        printTabuleiro(tabuleiro)
    else:
        printTabuleiro(root.estadoAtual)

    if root is None:
        root= Node(tabuleiro, None, 0,0 )
        print("FOram testadas", counter, "possibilidades")
    maior_indice = 0
    for i in range(len(root.children)):
        if (root.children[i].evaluation > root.children[maior_indice].evaluation):
            maior_indice= i
        if (root.children[i].winner == 0):
            maior_indice=i
            break
    root = root.children[maior_indice]
    if (root.winner is not None):
        break
#root = Node(tabuleiro, None, 0, 0)
print("------------------")
printTabuleiro(root.estadoAtual)
if root.winner == 0:
    print("A Máquina ganhou!")
elif root.winner == 1:
    print("Você ganhou!")
else:
    print("Empate!")

