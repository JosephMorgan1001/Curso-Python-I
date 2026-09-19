from os import system
system('cls')
import time
#inicia a contagem
for i in range(1,11):
    #limpa a variavel
    linha = ''
    for ii in range(1, 11):
        #vai armazenanndo toda tabuada
        linha += f'{i * ii: >4} ' # >4 conta os caracteres totais e mostra 3 com espaços vazios a esquerda
    print(linha)
    time.sleep(0.5)