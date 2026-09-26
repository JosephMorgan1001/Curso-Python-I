from os import system
system('cls')
import random

continua = 'S'

while continua == 'S':

    computador = random.randint(0,2)

    print('\n 0 = pedra \n 1 = papel \n 2 = tesoura')
    #ou
    #input('''test
    #test
    #test ''') USAR (''' ''') permite  colocar em linha diferente sem usar o \n

    player = int(input('escolha um número:  ')) 
    system('cls')

    if player >= 0 and player <= 2:
        pecas = ['pedra', 'papel', 'tesoura']
        print(f'O Agente escolheu: {pecas[computador]}')
        print(f'Você escolheu {pecas[player]}')


        tabela = ((0, 1 ,-1), (-1 ,0 ,1), (1, -1 ,0))
        jogada = tabela[computador][player]

        if jogada == -1:
            print('perdeu filhão')
        elif jogada == 0:
            print('empate filhão')
        elif jogada == 1:
            print('AEEEEE, GANHOU!!!! 😊😊')
    else:
        print('Player choose number is incorret')
    continua = input('Digite [S] para jogar novamente.').upper()