from os import system
system('cls')
from datetime import datetime

#class sempre é POO :)
today = datetime.today()
class  Servico:
    def __init__(self, descricao, preco):
        self.descricao = descricao
        self.preco = preco

    def exibir_dados(self):
        print(f'Descrição: {self.descricao}')
        print(f'Preco: {self.preco:.2f}')
    #metodo para salvar dados em txt
    def salvar_historico(self):
        #abre o arquivo em modo de escrita (append)
        with open('historico_servicos.txt', 'a', encoding='utf-8') as f:
            f.write(f'Descrição: {self.descricao}\n')
            f.write(f'Preço: {self.preco:.2f}\n')
            f.write(f'Data e Hora: {today.strftime('%d/%m/%Y  %H:%M:%S')}\n')
            f.write('\n' + '-' * 40 + '\n')

#Iniciando o código principal
print(10 * '-' +  ' ' + 'Cadastrado de serviço' + ' ' + 10 * '-')

continuar = 'S'

while continuar.upper() != 'X':
    descricao = input('Informe a descrição do serviço: ')
    preco = input('Informe o valor do serviço: ')

    try:
        preco = float(preco)
    except ValueError:
        print('Digite um número válido')
        continue

#criando uma instância da classe Servico
    servico = Servico(descricao, preco)

    #Exibindo os dados do serviço
    servico.exibir_dados()
    #salvar dados em arquivo TXT
    servico.salvar_historico()
    print('-' * 40)
    continuar = input('Tecle qualquer tecla para continuar ou X para parar')