import numpy as np
import copy

matriz_jogo = [[0,0,0],[0,0,0],[0,0,0]]
jogo_da_velha = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

def objetivo(matriz):
    aux = 0
    for linha in range(3):
        for coluna in range(3):
            if(matriz[linha][coluna] == 0):
                aux = aux + 1

    for linha in range(3):
        contador = 0
        for coluna in range(3):
            contador=contador + matriz[linha][coluna]
        if (contador == 3):
            return 1
        if (contador == -3):
            return -1

    for coluna in range(3):
        contador = 0
        for linha in range(3):
            contador = contador + matriz[linha][coluna]
        if(contador == 3):
            return 1
        if(contador == -3):
            return -1

    if(matriz[0][0] + matriz[1][1] + matriz[2][2] == 3):
        return 1
    elif(matriz[0][0] + matriz[1][1] + matriz[2][2] == -3):
        return -1
    if(matriz[2][0] + matriz[1][1] + matriz[0][2] == 3):
        return 1
    elif(matriz[2][0] + matriz[1][1] + matriz[0][2] == -3):
        return -1
    if(aux == 0):
        return 0
    return -2

def gerador_minimax(matriz, jogador):
    resultado = []
    for linha in range(3):
        for coluna in range(3):
            if(matriz[linha][coluna] == 0):
                next_matriz = copy.deepcopy(matriz)
                next_matriz[linha][coluna] = jogador
                resultado.append(next_matriz)
    return resultado

def minimax(matriz, maximo):
    valor_objetivo = objetivo(matriz)
    if valor_objetivo in [1, 0, -1]:
        return valor_objetivo
    if(maximo == True):
        gerador_max = gerador_minimax(matriz, 1)
        retorno_max = -1000
        for k in gerador_max:
            retorno_max = np.max([retorno_max, minimax(k, False)])
        return retorno_max

    if(maximo == False):
        gerador_minimax_children = gerador_minimax(matriz, -1)
        retorno_mini = 1000
        for k in gerador_minimax_children:
            retorno_mini = np.min([retorno_mini, minimax(k, True)])
        return retorno_mini

def jogada_maquina(matriz): #Etapa da IA
    gerador = gerador_minimax(matriz, -1)
    for k in gerador:
        if(minimax(k,True) == -1):
            return k
    for k in gerador:
        if(minimax(k,True) == 0):
            return k

print("Você inicia jogando com X e a máquina com O.")
print("Obs: As linhas e colunas vão de 0 a 2.")
while(objetivo(matriz_jogo) == -2):
    print("\nDigite linha e a coluna da sua jogada:")
    linha, coluna = input().split(" ")
    linha = int(linha)
    coluna = int(coluna)
    if(jogo_da_velha[linha][coluna] == "X" or jogo_da_velha[linha][coluna] == "O"):
        print("\nJogada inválida, a posição já está marcada. Jogue novamente.")
        continue
    matriz_jogo[linha][coluna] = 1
    print("\nVez da máquina.")
    matriz_jogo = jogada_maquina(matriz_jogo)
    for i in range(3):
        for j in range(3):
            if(matriz_jogo[i][j] == -1):
                jogo_da_velha[i][j] = "O"
            elif(matriz_jogo[i][j] == 1):
                jogo_da_velha[i][j] = "X"
    print('\n', jogo_da_velha[0], '\n', jogo_da_velha[1], '\n', jogo_da_velha[2])
    #print('\n', matriz_jogo[0], '\n', matriz_jogo[1], '\n', matriz_jogo[2])

if(objetivo(matriz_jogo) == -1):
    print("Você foi derrotado!   :(")
if(objetivo(matriz_jogo) == 0):
    print("Empate!   :|")
if(objetivo(matriz_jogo) == 0):
    print("Você venceu!!!!   :D")