estado = dict()
brasil = list()

for c in range(0, 1):
    estado['es'] = str(input('Nome do estado: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()