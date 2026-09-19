from os import system
system('cls')

numeros = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove')
dez = ('dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove')
dezenas = ('vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa')

n1 = int(input('digite um número de 0 a 99: '))

if n1 >= 0 and n1 <= 99:
    if numeros < 10:
        print(numeros[numeros])
    elif numeros < 20:
        print(dez[numeros-10])
else:
    print('num invalido')