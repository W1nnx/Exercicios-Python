import random
from time import sleep

resultado = dict()
jogadores = list()

print('Valores sorteados:')

for c in range(0, 4):
    r = random.randint(1, 6)
    resultado["Jogador"+str(c+1)] = r
    jogadores.append(r)

    print(f'O {"Jogador"+str(c+1)} tirou {r}')

jogadores.sort(reverse= True)
jogar = 't'

print('-='*15)
print(' == RANKING DOS JOGADORES == ')

for p in range(0,4):
    print(f'{p+1}º Lugar: ', end='')
    for k, v in resultado.items():
        if v == jogadores[p] and jogar != k:
            sleep(0.1)
            print(k,'com',v)
            jogar = k
            break