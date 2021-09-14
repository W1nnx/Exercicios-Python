import random

r = random.randint(1, 10)

cont = 0

player = ''
while player != r:
    pc = random.randint(1, 10)
    player = int(input('Qual numero voce escolhe? '))
    cont += 1

    if player == r:
        print('Voce venceu')
    else:
        print('Numero incorreto tente outro')

    if pc == r:
        print('O computador venceu')

print(f'Voce tentou {cont} vezes ate acertar')












