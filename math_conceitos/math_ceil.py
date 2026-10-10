from os import system
system('cls')
import math

#uma loja precisa armazenar seus produtos em caixas.
# cada caixa pode conter no máximo ?? produtos.

num_produtos = int(input('Informe o número dos produtos: '))
produtos_caixa = int(input('Informe a quantidade de produtos por caixa: '))

qtd_caixas = (math.ceil(num_produtos / produtos_caixa))
print(f'Quantidades de caixas necessárias: {qtd_caixas}')