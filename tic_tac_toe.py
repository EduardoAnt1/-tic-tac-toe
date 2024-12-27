import numpy as np
import sys

tam = 3
jogo = np.zeros((tam,tam))
dimensao = tam**2


def print_jogo():
    for i in range(tam):
        print("\n")
        print("___",end= "")
        print("___",end= "")
        print("___",end= "")
        print("___",end= "")
        print("\n")
        print("|",end= " ")
        for j in range(tam):
            if jogo[i][j] == 1:
                print("X",end= " ")
            elif jogo[i][j] == 2: 
                print("O",end= " ")
            else:
                print(" ",end= " ")
            print("|",end= " ")
            
def venceu():
    for i in range(tam):
        if (jogo[i][0] == jogo[i][1] == jogo[i][2]) and jogo[i][0]!=0:
            return True
        elif (jogo[0][i] == jogo[1][i] == jogo[2][i]) and jogo[0][i]!=0:
            return True
    if (jogo[0][0] == jogo[1][1] == jogo[2][2]) and jogo[0][0]!=0:
        return True
    elif (jogo[0][2] == jogo[1][1] == jogo[2][0]) and jogo[0][2]!=0:
        return True
    else:
        return False

def velha():
    for i in range(tam):
        for j in range(tam):
            if(jogo[i][j] == 0):
                return False
    return True
        
    
for i in range(dimensao):
    for j in range(2):
        print_jogo()
        jogador_x,jogador_y = input(f"\njogador {j+1} digite a linha e a coluna que quer jogar").split()
        j_x = int(jogador_x)
        j_y = int(jogador_y)
        if(jogo[j_x-1][j_y-1] == 0):
            if(j == 0):
                jogo[j_x-1][j_y-1] = 1
            elif(j == 1):
                jogo[j_x-1][j_y-1] = 2
        else:
            print("Posição já ocupada!")
            j-=1
            continue
        if(venceu()):
            print(f"\njogador {j+1} venceu!")
            sys.exit()
        if(velha()):
            print("\nDeu velha!")
            sys.exit()
        
    