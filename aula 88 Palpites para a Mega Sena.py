from random import sample
jogos = list()

print('-'*20)
print('JOGAR NA MEGA SENA')
print('-'*20)

sorteiojg = int(input('Quantos jogos vc quer sortear? '))

print(f'-=-=-=  SORTEANDO {sorteiojg} JOGOS  -=-=-=')
for s in range(sorteiojg):
    jg = sorted(sample(range(1, 61), 6))
    jogos.append(jg[:])
    print(f'Jogo {s+1}: {jg}')