import os

"""
    Matriz global que representa o tabuleiro do jogo;
"""
global matriz
matriz = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


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
    for i in range(0,3):
        print("\t", end='')
        for j in range(0,3):
            if j == 2:
                print(" %c" %matriz[i][j] + " ")
            else:
                print(" %c" %matriz[i][j] + " |", end='')
        if i == 2:
            print()
        else:
            print("\t---|---|---")


"""
    Função que executa o movimento pedido pelo jogador;
    Função sem valor de retorno;
"""
def jogada(pos, player):
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
        print("\n   Movimento invalido, tente novamente!");
        aux = int(input("   Digite o valor de uma posicao no tabuleiro: "))
        jogada(aux, player);
    
    if matriz[x][y] != ' ':
        print("\n   Movimento invalido, tente novamente!");
        aux = int(input("   Digite o valor de uma posicao no tabuleiro: "))
        jogada(aux, player);
    else:
        matriz[x][y] = player


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


"""
    Função principal, que chama as funções necessárias para o jogo;
    Função sem valor de retorno;
"""
def main():
    print("   Bem vindo(a) ao Jogo da Velha da Oficina de Teoria dos Jogos!")
    check = ' '
  
    while check == ' ':
        posicoes()
        mapa()
        pos = int(input("   Player 1 jogando...\n\n   Digite o valor de uma posicao no tabuleiro: "))
        jogada(pos, 'O')
        check = verificar()
        if check != ' ':
            break
        if velha() == True:
            break
        os.system('cls' if os.name == 'nt' else 'clear')
        posicoes()
        mapa()
        pos = int(input("   Player 2 jogando...\n\n   Digite o valor de uma posicao no tabuleiro: "))
        jogada(pos, 'X')
        check = verificar()
        if velha() == True:
            break
        os.system('cls' if os.name == 'nt' else 'clear')
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n")
    mapa()

    if check == 'O':
        print("\tJogador 1 venceu!!\n")
    elif check == 'X':
        print("\tJogador 2 venceu!!\n")
    else:
        print("\tDeu velha!!\n")

    a = input("\n\n\nPressione qualquer tecla para encerrar!")


#----------------------------------
main()