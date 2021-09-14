dados = dict()
lista = list()
soma = media = 0
c = 0

while True:
    dados.clear()

    dados['nomes'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo: (M / F) '))

    c += 1

    while not dados['sexo'] in 'MmFf':
        print('ERRO! Por Favor, digite apenas M ou F')
        dados['sexo'] = str(input('Sexo: (M / F) '))

    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']

    lista.append(dados.copy())

    continuar = ' '
    while not continuar in 'SsNn':
        continuar = str(input('Quer continuar? (S/N) '))
    if continuar in 'Nn':
        break

print(f'A) Ao todo temos {c} pessoas cadastradas')

media = soma/len(dados)
print(f'B) A media de idade é de {media:5.2f}')
print(f'C) As mulheres cadastradas foram ', end='')
for p in lista:
    if p['sexo'] in 'Ff':
        print(f'{p["nomes"]} ',end='')
print()
print('D) Lista das pessoas que estao acima da media: ')
for p in lista:
    if p['sexo'] in 'Ff':
        print(' ', end='')
        for k,v in p.items():
            print(f'{k} = {v}: ', end='')
        print()
print('<< ENCERRADO >>')