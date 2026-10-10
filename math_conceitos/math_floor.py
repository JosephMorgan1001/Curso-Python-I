from os import system
system('cls')
import math
#um caminhão transporta ?? toneladas de carga.
# Quantas viagens ele precisa fazer somente com capacidade máxima 

capacidade_total = int(input('Carga total do caminhão (em toneladas): '))
carga_viagem = float(input('Carga para viagem (em toneladas): '))

qtd_viagem = math.floor(carga_viagem / capacidade_total)
carga_restante = carga_viagem - (capacidade_total * qtd_viagem)

print(f'Quantidade de viagens carga máxima: {qtd_viagem}')
print(f'Quantidade carga restante: {carga_restante:.2f}')
