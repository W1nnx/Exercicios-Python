'''''
                Dividindo valores em várias listas

lista = []
pares = []
impar = []

while True:
    numero = int(input("Digite um numero: "))
    lista.append(numero)

    continuar = ' '
    while continuar not in 'SsNn':
        continuar = input('Quer continuar? [S/N] ')

    if continuar in 'Nn':
        break

print(f'A lista completa é {lista}')

for n in range(0, len(lista)):
    if lista[n] % 2==0:
        pares.append(lista[n])
    else:
        impar.append(lista[n])
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impar}')
'''''






#
















































































































































































