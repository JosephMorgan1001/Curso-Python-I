from os import system
system('cls')
import random
from datetime import datetime

class Personagem:
    def __init__ (self, nome, energia, dano):
        self.nome = nome
        self.energia = energia
        self.dano = dano

    def atacar(self, inimigo):
        energia_anterior = inimigo.energia
        inimigo.energia -= self.dano
        #evita energia ficar negativa
        inimigo.energia = max(inimigo.energia, 0)
        print(f'{self.nome} atacou {inimigo.nome} causando {self.dano} de dano!\n')
        print(f'{inimigo.nome} tinha {energia_anterior} agora tem {inimigo.energia} de energia restante. \n')

        if inimigo.energia == 0:
            print(f'{inimigo.nome} foi derrotado por {self.nome}\n')
            return True
        
print('-' * 40)
print('Bem vindo ao jogo de batalha!')
print('-' * 40)

#criação de personagens
mago = Personagem("Mago", 95, 25)
guerreiro = Personagem('Guerreiro', 120, 15)
ladrao = Personagem('Ladrão', 100, 20)
aleatorio = Personagem('Aleatorio', random.randint(80,150), random.randint(10,25))

while True:
    atacar = random.choice([mago, guerreiro, ladrao, aleatorio])
    if atacar == mago:
        atacado = random.choice([guerreiro, ladrao, aleatorio])
    elif atacar == guerreiro:
        atacado = random.choice([mago, ladrao, aleatorio])
    elif atacar == ladrao:
        atacado = random.choice([guerreiro, mago, aleatorio])
    else:
        atacado = random.choice([guerreiro, mago, ladrao])

    if atacar.atacar(atacado) == True:
        break

#ataques
mago.atacar(guerreiro)
guerreiro.atacar(aleatorio)
aleatorio.atacar(ladrao)
ladrao.atacar(mago)

