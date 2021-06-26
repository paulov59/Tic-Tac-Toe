import os
import pygame
from pygame import font
#from pygame.locals import *
from sys import exit


#try: 
pygame.init()
#except: print("Erro. Pygame não inicializou.")
weight = 480
height = 480
screen = pygame.display.set_mode((weight, height))

#rect1 = Rect((0,0), (weight/3,height/3))
#rect2 = Rect((weight/3,0), ((weight/3)*2,height/3))
#rect3 = Rect(((weight/3)*2,0), (weight,height/3))
#rect4 = Rect((0,height/3), (weight/3,height/3))
#rect5 = Rect((weight/3,height/3), ((weight/3)*2,height/3))
#rect6 = Rect(((weight/3)*2,height/3), (weight,height/3))
#rect7 = Rect((0,(height/3)*2), (weight/3,(height/3)*2))
#rect8 = Rect((weight/3,(height/3)*2), ((weight/3)*2,(height/3)*2))
#rect9 = Rect(((weight/3)*2,(height/3)*2), (weight,(height/3)*2))

"""
    Matriz global que representa o tabuleiro do jogo;
"""
global matriz
matriz = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

"""
    Função que verifica se o movimento continuará a partidad ou resultará em vitória, empate ou derrota;
    Retorna um inteiro que representa a "pontuação" do tabuleiro, onde 10 representa vitória, -10 derrota e 0 empate;
"""
def dar_valor(cpu, player):
    for i in range(0,3):
        if matriz[i][0] == matriz[i][1] == matriz[i][2]:
            if matriz[i][0] == cpu: 
                return 10 
            elif matriz[i][0] == player:
                return -10

    for j in range(0,3):
        if matriz[0][j] == matriz[1][j] == matriz[2][j]:
            if matriz[0][j] == cpu: 
                return 10
            elif matriz[0][j] == player:
                return -10
                
    if matriz[0][0] == matriz[1][1] == matriz[2][2]:
        if matriz[0][0] == cpu:
            return 10
        elif matriz[0][0] == player:
            return -10
            
    if matriz[0][2] == matriz[1][1] == matriz[2][0]:
        if matriz[0][2] == cpu:
            return 10
        elif matriz[0][2] == player:
            return -10
            
    return 0


"""
    Função que verifica se ainda há movimentos disponíveis;
    Retorna um valor booleano informando se há ou não movimentos;
"""
def tem_movimentos_restantes():
	for i in range(0,3):
		for j in range(0,3):
			if matriz[i][j] == ' ':
				return True
	return False


"""
    Função que calcula a melhor posição a ser jogada;
    Retorna um inteiro que representa a "pontuação" da casa desejada, onde 10 representa vitória, -10 derrota e 0 empate;
"""
def minimax(profundidade, isMax, cpu):
    player = 'O'
    if cpu == 'O':
        player = 'X'

    score = dar_valor(cpu, player)
    if score == 10:
        return score

    if score == -10:
        return score

    if tem_movimentos_restantes() == False:
        return 0 

    if isMax == True:
        best = -1000
        for i in range(0,3):
            for j in range(0,3):
                if matriz[i][j] == ' ':
                    matriz[i][j] = cpu
                    best = max(best, minimax(profundidade+1, not isMax, cpu))
                    matriz[i][j] = ' '
        return best 

    else:
        best = 1000
        for i in range(0,3):
            for j in range(0,3):
                if matriz[i][j] == ' ':
                    matriz[i][j] = player
                    best = min(best, minimax(profundidade+1, not isMax, cpu))
                    matriz[i][j] = ' '
        return best  

"""
    Função que encontra a melhor posição a ser jogada pela CPU;
    Retorna uma lista com o valor da linha e coluna do movimento;
"""
def melhor_movimento(cpu):
    bestValue = -1000; move = [-1,-1]
    for i in range(0,3):
        for j in range(0,3):
            if matriz[i][j] == ' ':
                matriz[i][j] = cpu
                moveValue = minimax(0, False, cpu)
                matriz[i][j] = ' '
                if moveValue > bestValue:
                    move[0] = i
                    move[1] = j
                    bestValue = moveValue

    return move


"""
    Função que imprime as posições do tabuleiro;
    Função sem valor de retorno;
"""
def posicoes():
    aux = 7
    print("   Posicoes do jogo:\n")
    for i in range(0,3):
        print("\t", end='')
        for j in range(0,3):
            if j == 2:
                print(" %d" %aux)
                aux = 3 if i == 0 else 0
            else:
                print(" %d" %aux + " |", end='')
            aux += 1
        if i == 2:
            print()
        else:
            print("\t---|---|---")


"""
    Função que imprime o estado atual do tabuleiro;
    Função sem valor de retorno;
"""
def mapa():
    delta_xy = 30
    x = y = 0
    img_o = pygame.image.load("o.png")
    img_x = pygame.image.load("x.png")
    img_o = pygame.transform.scale(img_o, (int(weight/3-delta_xy), int(height/3-delta_xy)))
    img_x = pygame.transform.scale(img_x, (int(weight/3-delta_xy), int(height/3-delta_xy)))
    #print("imgs=", img_x, img_o)
    for i in range(0,3):
        for j in range(0,3):
            if (matriz[i][j]=='X'):
                screen.blit(img_x, (x+delta_xy/2, y+delta_xy/2))
            elif matriz[i][j]=='O':
                screen.blit(img_o, (x+delta_xy/2, y+delta_xy/2))
            x += weight/3
            pygame.display.flip()
        y += height/3
        x = 0
    y = 0
    #print("MATRIZ=", matriz)


"""
    Função que executa o movimento proposto pela CPU;
    Função sem valor de retorno;
"""
def jogadaCPU(x, y, cpu):
    matriz[x][y] = cpu


"""
    Função que executa o movimento pedido pelo jogador;
    Função sem valor de retorno;
"""
def jogada(pos, player):
    x = y = 0
    if pos == 7:
        x = 0; y = 0;
    elif pos == 8:
        x = 0; y = 1;
    elif pos == 9:
        x = 0; y = 2;
    elif pos == 4:
        x = 1; y = 0;
    elif pos == 5:
        x = 1; y = 1;
    elif pos == 6:
        x = 1; y = 2;
    elif pos == 1:
        x = 2; y = 0;
    elif pos == 2:
        x = 2; y = 1;
    elif pos == 3:
        x = 2; y = 2;
    else:
        #print("Movimento invalido, tente novamente!\n");
        #aux = int(InputPosPlayer())
        #jogada(aux, player);
        return -1
    
    if matriz[x][y] != ' ':
        #print("Movimento invalido, tente novamente!\n");
        #aux = int(InputPosPlayer())
        #jogada(aux, player);
        return -1
    else:
        matriz[x][y] = player
        return 1


"""
    Função que verifica o vencedor da partida;
    Retorna o caracter usado pelo vencedor ou um espaço, representando que o jogo está em andamento;
"""
def verificar():
    for i in range(0,3):
        if matriz[i][0] == matriz[i][1] == matriz[i][2]:
            return matriz[i][0]

    for i in range(0,3):
        if matriz[0][i] == matriz[1][i] == matriz[2][i]:
            return matriz[0][i]

    if matriz[0][0] == matriz[1][1] == matriz[2][2]:
        return matriz[0][0]

    if matriz[0][2] == matriz[1][1] == matriz[2][0]:
        return matriz[0][2]

    return ' '


"""
    Função que verifica se houve empate no jogo;
    Retorna um valor booleano;
"""
def velha():
    for i in range(0,3):
        for j in range(0,3):
            if matriz[i][j] == ' ':
                return False
    return True


def DrawTable():
    width = 10
    pygame.draw.line(screen, (255, 255, 255), (0, height/3), (weight, height/3), width)
    pygame.draw.line(screen, (255, 255, 255), (0, (height/3)*2), (weight, (height/3)*2), width)
    pygame.draw.line(screen, (255, 255, 255), (weight/3, 0), (weight/3, height), width)
    pygame.draw.line(screen, (255, 255, 255), ((weight/3*2), 0), ((weight/3)*2, height), width)


def DrawTexts(text="Hello world!\0", size=10, dx=int(20), dy=int(20)):
    font.init()
    name_font = font.get_default_font()
    sys_font = font.SysFont(name_font, size)
    txt_scr = sys_font.render(text, 1, (255, 255, 255))
    screen.blit(txt_scr, (weight/2-dx, height/2-dy))


def InputPlayer():
    for event in pygame.event.get():
        #if (event.type==pygame.QUIT):
            #pygame.exit()
            #exit()
        if (event.type==pygame.KEYDOWN):
            if event.key==pygame.K_x: return 'X'
            elif event.key==pygame.K_o: return 'O'
            elif (event.key==pygame.K_s): return 'S'
            elif (event.key==pygame.K_n): return 'N'
        elif (event.type==pygame.KEYUP):
            if event.key==pygame.K_x: return 'X'
            elif event.key==pygame.K_o: return 'O'
            elif (event.key==pygame.K_s): return 'S'
            elif (event.key==pygame.K_n): return 'N'
    return ' '


def DrawInstru():
    margin = int(8)
    DrawTexts("Digite 7.", 20, weight/2-margin, height/2-margin)
    DrawTexts("Digite 8.", 20, (weight/3)/2-margin, height/2-margin)
    DrawTexts("Digite 9.", 20, -(weight/3)/2-margin, height/2-margin)
    DrawTexts("Digite 4.", 20, weight/2-margin, (height/3)/2-margin)
    DrawTexts("Digite 5.", 20, (weight/3)/2-margin, (height/3)/2-margin)
    DrawTexts("Digite 6.", 20, -(weight/3)/2-margin, (height/3)/2-margin)
    DrawTexts("Digite 1.", 20, weight/2-margin, -(height/3)/2-margin)
    DrawTexts("Digite 2.", 20, (weight/3)/2-margin, -(height/3)/2-margin)
    DrawTexts("Digite 3.", 20, -(weight/3)/2-margin, -(height/3)/2-margin)


def InputPosPlayer():
    for e in pygame.event.get():
        if e.type==pygame.KEYDOWN:
            if e.key==pygame.K_KP0 or e.key==pygame.K_0: return 0
            elif e.key==pygame.K_KP1 or e.key==pygame.K_1: return 1
            elif e.key==pygame.K_KP2 or e.key==pygame.K_2: return 2
            elif e.key==pygame.K_KP3 or e.key==pygame.K_3: return 3
            elif e.key==pygame.K_KP4 or e.key==pygame.K_4: return 4
            elif e.key==pygame.K_KP5 or e.key==pygame.K_5: return 5
            elif e.key==pygame.K_KP6 or e.key==pygame.K_6: return 6
            elif e.key==pygame.K_KP7 or e.key==pygame.K_7: return 7
            elif e.key==pygame.K_KP8 or e.key==pygame.K_8: return 8
            elif e.key==pygame.K_KP9 or e.key==pygame.K_9: return 9
        elif e.type==pygame.KEYUP:
            if e.key==pygame.K_KP0 or e.key==pygame.K_0: return 0
            elif e.key==pygame.K_KP1 or e.key==pygame.K_1: return 1
            elif e.key==pygame.K_KP2 or e.key==pygame.K_2: return 2
            elif e.key==pygame.K_KP3 or e.key==pygame.K_3: return 3
            elif e.key==pygame.K_KP4 or e.key==pygame.K_4: return 4
            elif e.key==pygame.K_KP5 or e.key==pygame.K_5: return 5
            elif e.key==pygame.K_KP6 or e.key==pygame.K_6: return 6
            elif e.key==pygame.K_KP7 or e.key==pygame.K_7: return 7
            elif e.key==pygame.K_KP8 or e.key==pygame.K_8: return 8
            elif e.key==pygame.K_KP9 or e.key==pygame.K_9: return 9
    return -1

"""
    Função principal, que chama as funções necessárias para o jogo;
    Função sem valor de retorno;
"""
def main():
    #DrawTable()
    DrawTexts("Tic-Tac-Toe", 70, 120, 120)
    DrawTexts("Por favor, selecione X ou O.", 30, 125, 0)
    pygame.display.flip()

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Bem vinda(o) ao Jogo da Velha da Oficina de Teoria dos Jogos!")
    check = ' '
    player = InputPlayer()
    while player != 'X' and player != 'O':
        print("Opção inválida!")
        player = InputPlayer()
    
	#New display:
    screen = pygame.display.set_mode((weight, height))
    DrawTexts("Tic-Tac-Toe", 70, 120, 120)
    DrawTexts("Deseja começar primeiro[s,n]?", 30, 140, 0)
    pygame.display.flip()

    cpu = 'O'
    if player == 'O':
        cpu = 'X'

    op = InputPlayer()
    while op != 'S' and op != 'N':
        print("Opção inválida!")
        #os.system('cls' if os.name == 'nt' else 'clear')
        op = InputPlayer()

    #New thirdty display:
    screen = pygame.display.set_mode((weight, height))
    DrawTable()
    DrawInstru()
    pygame.display.flip()

    if op == 'S':
        os.system('cls' if os.name == 'nt' else 'clear')
        posicoes()
        mapa()

        pos = int(InputPosPlayer())
        while jogada(pos, player)!=1:
            pos = int(InputPosPlayer())

        jogada(pos, player)
        mapa()

    while check == ' ':
        #new screen:
        screen = pygame.display.set_mode((weight, height))
        DrawTable()
        DrawInstru()        
        pygame.display.flip()

        posCPU = melhor_movimento(cpu)
        jogadaCPU(posCPU[0], posCPU[1], cpu)
        check = verificar()
        if check != ' ':
            break
        if velha() == True:
            break
        os.system('cls' if os.name == 'nt' else 'clear')
        posicoes()
        mapa()

        pos = int(InputPosPlayer())
        while jogada(pos, player)!=1:
            pos = int(InputPosPlayer())

        if velha() == True:
            break
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n")
    mapa()
    pygame.display.flip()

    if check == cpu:
        print("\tCPU venceu!!\n")
    elif check == player:
        print("\tParabéns, você venceu!!\n")
    else:
        print("\tDeu velha!!\n")
    #pygame.time.wait(4000)
    #for event in pygame.event.get():
    #    if event.type==pygame.KEYDOWN:
    #        if event.type==pygame.QUIT:
    pygame.quit()
                #sys.exit()


#----------------------------------
main()
