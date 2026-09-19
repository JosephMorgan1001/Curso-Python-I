#desconto de salario inss
from os import system
system('cls')

salario = float(input('Digite seu sálario: '))

if salario <= 1621:
    descontoinss = salario * 0.075
    print(f'Seu desconto do INSS {descontoinss:.2f}')
    print(f'Seu salario líquido é {salario - descontoinss:.2f}')
elif salario > 1621 and salario <= 2902.84:
    descontoinss = salario * 0.09 - 24.32
    print(f'Seu desconto do INSS {descontoinss:.2f}')
    print(f'Seu salario líquido é {salario - descontoinss:.2f}')
elif salario > 2902.84 and salario <= 4354.27:
    descontoinss = salario * 0.12 - 111.41
    print(f'Seu desconto é de: {descontoinss:.2f}')
    print(f'Seu salario líquido é {salario - descontoinss:.2f}')
elif salario > 4354.28 and salario <= 8475.55:
    descontoinss = salario * 0.14 - 198.5
    print(f'Seu desconto é de {descontoinss:.2f}')
    print(f'Seu salario líquido é de {salario - descontoinss:.2f}')
elif salario > 8475.55:
    descontoinss = 988.07
    print(f'Seu desconto é de {descontoinss:.2f}')
    print(f'Seu salário líquido é de: {salario - descontoinss:.2f}')
else:
    print('tente de novo')


liquido = salario - descontoinss
if liquido <= 2428.80:
    print('Isento de imposto de renda')
elif liquido >= 2428.81 and liquido <= 2826.65:
    descontoir = liquido * 0.075 - 182.16
    print(f'\nSeu desconto de irpf é de: {descontoir:.2f}')
    print(f'\nSeu salario liquido é de com irpf {liquido - descontoir:.2f}')
elif liquido > 2826.66 and liquido <= 3751.05:
    descontoir = liquido * 0.15 - 394.16
    print(f'Seu desconto de irpf é de {descontoir:.2f}')
    print(f'Seu salario liquido é de com irpf {liquido - descontoir:.2f}')
elif liquido > 3751.06 and liquido <= 4664.68:
    descontoir = liquido * 0.225 - 675.49
    print(f'Seu salario liquido é de com irpf {liquido - descontoir:.2f}')
    print(f'Seu desconto de irpf é de {descontoir:.2f}')
elif liquido > 4664.69:
    descontoir = liquido * 0.275 - 908.73
    print(f'Seu desconto de irpf é de {descontoir:.2f}')
    print(f'\nSeu salario liquido é de com irpf {liquido - descontoir:.2f}')
