from os import system
system('cls')
import time

n1 = int(input('Digite seu numero:'))

if n1 < 0:
    print('Num invalido')
elif n1 > 0:

    for i in range(n1):
        print(f'O contador vai contar: {i} ')
        time.sleep(0.1)
