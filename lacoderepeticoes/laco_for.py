from os import system 
system('cls')
import time #importar o time.sleep(segundos que você quer que vá mais lento)

n1 = int(input('Digite um numero > 0: '))

if n1 <= 0: #Se o numero menor que zero
    print('num invalido') #diga que o numero foi invalido
elif n1 > 0: #caso contrário, número maior que zero
    for i in range(n1): # Para os números dentro do sequência/range 
        print(f'O contador vai contar: {i}') #conte quantos números tem 
        time.sleep(0.1) #pausa 2s
