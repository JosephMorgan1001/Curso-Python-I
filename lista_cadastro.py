from os import system
system('cls')



clientes = []
telefones = [] 
opcao = ''

while opcao.upper() != 'X':
    nome = input("Digite o nome do cliente: ")
    telefone = input('Digite o telefone do cliente: ')

    clientes.append(nome)
    telefones.append(telefone)

    system('cls')
    print('Cadastro realizado com sucesso! ')
    opcao = input('Aperte X para finalizar o programa ou qualquer tecla para continuar')

system('cls')


for i in range(len(clientes)):
    print(f'Nome: {clientes[i]} | Telefone: {telefones[i]}')
