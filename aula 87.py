matriz = [[], [], []]
pares = 0
colunas = 0

for l in range(0, 3):
    for c in range(0, 3):
        valores = int(input(f'Digite um valor para [{l}, {c}]: '))
        matriz[l].append(valores)

        if valores % 2==0:
            pares += valores

        if c == 2:
            colunas += valores

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print(f'A soma de todos os valores pares sao {pares}')
print(f'A soma dos valores da terceira coluna sao {colunas}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')