list = [[], []]

for n in range(1,8):
    valor = int(input(f'Digite o {n}o valor: '))

    if valor % 2==0:
        list[0].append(valor)
    else:
        list[1].append(valor)

print('-=-'*15)
print(f'Os valores pares foram {sorted(list[0])}')
print(f'Os valores pares foram {sorted(list[1])}')