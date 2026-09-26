from os import system
system('cls')

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove')
dez = ('dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove')
dezenas = ('', '', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa')

n1 = int(input('digite um número de 0 a 99: '))

if n1 >= 0 and n1 <= 99:
    if n1 < 10:
        print(numeros[n1])
    elif n1 < 20:
        print(dez[n1-10])
    else:
        dezena = int(n1 / 10)
        numeral = n1 % 10
        if numeral == 0:
            print(dezenas[dezena])
        else:
            print(f'{dezenas[dezena]} e {numeros[numeral]}')
else:
    print('num invalido')




#Se n1 >= 0 and(e se) n1 < 99:
#
#
#
#
#
#
#