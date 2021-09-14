cadastro = dict()

cadastro['nome'] = str(input('Nome: '))
cadastro['idade'] = int(input('Ano de nascimento: '))
cadastro['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))

ctps = cadastro['CTPS']
nome = cadastro['nome']
idade = cadastro['idade']

if ctps != 0:
    cadastro['contrataçao'] = int(input('Ano de Contrataçao: '))
    cadastro['salario'] = int(input('Salario: R$'))

print('-='*15)
print(f'nome tem o valor {cadastro["nome"]}')
print(f'idade tem o valor {cadastro["idade"]}')
print(f'CTPS tem o valor {cadastro["CTPS"]}')
if ctps != 0:
    print(f'Contrataçao tem o valor {cadastro["contrataçao"]}')
    print(f'Salario tem o valor de {cadastro["salario"]}')
    print(f'Aposentadoria tem o valor {cadastro["contrataçao"] - idade + 35}')






































