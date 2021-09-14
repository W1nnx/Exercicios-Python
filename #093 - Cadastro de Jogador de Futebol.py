inf = dict()
total = 0

inf['nome'] = str(input('Nome do jogador: '))
inf['partidas'] = int(input(f'Quantas partidas {inf["nome"]} jogou: '))

inf['gols'] = list()

for c in range(inf['partidas']):
    inf['gols'].append(int(input(f'Quantos gols na partida {c}: ')))
    inf['total'] = sum(inf['gols'])

print('-=-'*15)
print(inf)
print('-=-'*15)

for k,v in inf.items():
    print(f'O campo {k} tem o valor {v}')

print('-=-'*15)
print(f'O jogador {inf["nome"]} jogou {inf["partidas"]} partidas.')

for c in range(0, inf['partidas']):
    print(f'=> Na partida {c}, fez {inf["gols"][c]}')
print(f'Foi um total de {inf["total"]} gols.')



















