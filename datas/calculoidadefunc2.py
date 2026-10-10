from os import system
system('cls')
from datetime import datetime

def calcular_idade(data_nascimento):
    data_atual = datetime.today()
    data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')

    idade = data_atual.year - data_nascimento.year
    return idade


def idade_dias(data_nascimento):
    data_atual = datetime.today()
    data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')

    #calculo
    idade_dias = (data_atual - data_nascimento).days
    return idade_dias

data_nascimento = input('Digite sua data de nascimento formato dd/mm/aaaa: ')
print(f'Sua idade é: {calcular_idade(data_nascimento)} anos')
print(f'Você já viveu: : {idade_dias(data_nascimento)} dias')