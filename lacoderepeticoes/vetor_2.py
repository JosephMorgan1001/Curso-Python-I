from os import system
system('cls')

#nomes = [] # cria lista vazia
#nomes.append(input('digite nome: ')) #o .append coloca mais nomes
#nomes.append(input('digite nome: '))
#nomes.append(input('digite nome: '))
#nomes.append(input('digite nome: '))
#nomes.append(input('digite nome: '))
#print(nomes)
nomes= []
total = int(input('Quantos nomes deseja cadastrar? '))
for i in range(0, total):
    nomes.append(input('Digite um nome: '))


for i in range(0, total):
    print(f'{i} - {nomes[i]}')