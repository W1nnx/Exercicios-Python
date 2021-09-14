from time import sleep

list = []
cont = 0

while True:
    list.append([])

    list[cont].append(str(input('Nome: ')))
    list[cont].append(float(input('Primeira nota: ')))
    list[cont].append(float(input('Segunda nota: ')))

    media = (list[cont][1] + list[cont][2]) / 2
    list[cont].append(media)

    continuar = input('Deseja continuar? [S/N] ')

    if continuar in 'Nn':
        break
    cont += 1

print('x+'*15)
print('Nº Nome        Media')
print('--'*15)

for pos, alun in enumerate(list):
    print(pos, f'{alun[0]:<15}', alun[3])

while True:
    print('--'*15)
    aluno = int(input('Deseja ver a nota do aluno? (Use 999 para finalizar) '))

    if aluno == 999:
        break
    else:
        print(f'As notas de {list[aluno][0]} são {list[aluno][1:3]}')
print('Finalizando...')
sleep(2)
print('Programa finalizado volte sempre')