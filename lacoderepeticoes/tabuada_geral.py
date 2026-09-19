from os import system
system('cls')

#inicia contagem do "multiplicando"
for i in range(1, 11):
    print(' ')
    print(f'Tabuada do {i}')
    print(' ')
    #inicia a contagem do "multiplicador"
    for ii in range(1, 11):
      #mostra e efetua a multiplicação
      print(f'{i} x {ii} = {i * ii}')
