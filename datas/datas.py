from datetime import datetime
from os import system
system('cls')

#print(datetime.now()) #mostra a data de agora

#data atual do sistema
data_atual = datetime.now()

#Criar data (Ano,Mês,Dia)
data_criada = datetime(2024, 9, 15) #pode complementar com o horário. Exemplo: datatime(2024, 9, 15, 20, 2, 18)
print(f'Data Criada: {data_criada}')

#Pedir data ao usuário:
data_usuario = input('Digite uma data no formato dd/mm/aaaa: ')
print(data_usuario)

#converter string para data
data_convertida = datetime.strptime(data_usuario, '%d/%m/%Y')


#apenas testes 
analise_data = datetime.now() - data_convertida
print(analise_data)

print(type(data_convertida))