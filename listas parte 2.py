'''pessoas = list()
dados = list()
dados.append('Win')
dados.append(15)
dados.append('Pedro')
dados.append(30)
pessoas.append(dados[:])
print(pessoas)'''




#   Lista composta e análise de dados


dados = []

nomes = []
pesos = []
while True:

    dados.append(input('Nomes: '))
    dados.append(float(input('Pesos: ')))

    nomes.append(dados[:])
    pesos.append(dados[1])
    dados.clear()

    continuar = ' '
    while continuar not in 'SsNn':
        continuar = input('Quer continuar? [S/N] ')

    if continuar in 'Nn':
        break

print('-=-'*15)

print(f'Ao todo, vc cadastrou {len(nomes)} pessoas.')
print(f'O maior peso foi {max(pesos)}Kg de ', end='')

for p in nomes:
    if p[1] == max(pesos):
        print(f'{p[0]}', end=' ')

print(f'\nO menor peso foi {min(pesos)}Kg de ', end='')
for p in nomes:
    if p[1] == min(pesos):
        print(f'{p[0]}', end=' ')

















































































































































