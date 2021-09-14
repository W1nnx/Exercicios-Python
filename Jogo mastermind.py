import random
from time import sleep

num = random.randrange(1000, 10000)

n = int(input('Adivinhe o número de 4 dígitos: '))

if n == 0000:
    print('Programa finalizando...')
    sleep(1)
    exit(0)

if (n == num):
    print('Excelente! Você adivinhou o número em apenas uma tentativa! Você é um Mastermind!')
else:
    ctr = 0

while n < 1000:
    n = int(input('Numero incorreto adivinhe o número de 4 dígitos: '))

while n > 10000:
    n = int(input('Numero incorreto adivinhe o número de 4 dígitos: '))

while (n != num):

    while n < 1000:
        n = int(input('Numero incorreto adivinhe o número de 4 dígitos: '))

    while n > 10000:
        n = int(input('Numero incorreto adivinhe o número de 4 dígitos: '))

    ctr += 1
    count = 0

    n = str(n)
    num = str(num)
    correct = ['X']*4

    for i in range(0, 4):
        if (n[i] == num[i]):
            count += 1
        else:
            continue

    if (count < 4) and (count != 0):
        print("Não é bem o número. Mas você obteve ", count ," dígito (s) correto (s)!")
        print("Além disso, esses números em sua entrada estavam corretos.")

        for k in correct:
            print(k, end=' ')
            print('\n')
            print('\n')
            n = int(input("Digite sua próxima escolha de números: "))

    elif (count == 0):
        print('Nenhum dos números em sua entrada corresponde.')
        n = int(input('Digite sua proxima escolha de numeros: '))

if n == num:
    print('Você se tornou um Mastermind!')
    print("Demorou apenas ", ctr," tentativas.")



