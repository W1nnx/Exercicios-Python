jogadores = dict()
partidas = list()
time = list()
while True:
    jogadores.clear()
    jogadores['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogadores["nome"]} jogou: '))
    partidas.clear()

    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))

    jogadores['gols'] = partidas[:]
    jogadores['total'] = sum(partidas)

    time.append(jogadores.copy())

    continuar = str(input('Quer continuar? (S/N) '))
    while not continuar in 'SsNn':
        print('ERRO! Por favor, digite apenas S OU N')
        continuar = str(input('Quer continuar? (S/N) '))

    if continuar in 'Nn':
        break

print('-=-'*14)

print('cod ',end='')
for i in jogadores.keys():
    print(f'{i:<15}',end='')
print()

for k, v in enumerate(time):
    print(f'{k:>3} ',end='')
    for d in v.values():
        print(f'{str(d):<16}',end='')
    print()
print('---'*14)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))

    if busca == 999:
        print('<<< Programa Finalizado >>>')
        break

    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o codigo {busca}!')
    else:
        print(f' --- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]} --- ')
        for n, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {n} fez {g} gols.')