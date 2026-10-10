from os import system
system('cls')
from datetime import datetime

#pedir data de nascimento:
data_nasc = input('Digite sua data de nascimento no formato dd/mm/aaaa: ')
#converter a data
data_convertida = datetime.strptime(data_nasc, '%d/%m/%Y')
#criar data atual em uma variavel
data_atual = datetime.today() #queremos pegar só hoje
#calculo, pegando apenas o ano:
calc_nasc = data_atual.year - data_convertida.year
#printar agora:
print(f'Sua idade atual é: {calc_nasc}')
