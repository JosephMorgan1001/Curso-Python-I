from os import system
system('cls')
from datetime import datetime

data_nasc = input('Digite sua data de nascimento no formato dd/mm/aaaa: ')
data_convertida = datetime.strptime(data_nasc, '%d/%m/%Y')


def calc_idade(data_nasc):
    data_atual = datetime.today() #queremos pegar só hoje
    

    #calcular idade:
    calc_nasc = data_atual.year - data_convertida.year
    return calc_nasc

print(f'Sua idade é: {calc_idade(data_nasc)}')