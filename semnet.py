'''''
import random

r = random.randint(1, 10)
tentativas = 0

while True:
    escolha = int(input('Escolha um numero de 1 a 10: '))

    tentativas += 1
    if tentativas == 5:
        print('Voce tentou muitas vezes e o programa foi finalizado')
        break

    if escolha == r:
        print('Parabens voce venceu')
    else:
        print('Numero incorreto tente outro')

    continuar = input('Deseja continuar? [S/N] ')

    if continuar in 'Nn':
        break
    else:
        continue
'''''


'''''
numero1 = int(input('Digite o primeiro numero: '))
elemento = input('Qual elemento para somar quer usar? ')
numero2 = int(input('Digite o segundo numero: '))

if elemento == '+':
    print(numero1+numero2)
if elemento == '-':
    print(numero1-numero2)
if elemento == '*' or elemento == 'x':
    print(numero1*numero2)
if elemento == '/':
    print(numero1/numero2)
if elemento == '%':
    print(numero1%numero2)
'''''


'''''
lista = []

while True:
    lista.append(input('Tecla: '))

    continuar = input('Deseja continuar? [S/N] ')

    if continuar in 'Nn':
        break
    else:
        continue
print(f'{lista}', end='')
'''''


'''''
import random

p = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

palavras = random.choice(p)

tentativas = 10
guesses = ' '


while tentativas > 0:

    erros = 0

    for char in palavras:

        if char in guesses:
            print(char)
        else:
            print("_")
            erros += 1

    if erros == 0:
        print('Voce perdeu')
        
        print('A palavra era', palavras)
        break

guess = input('Adivinhe o personagem: ')

guesses += guess

if guess not in palavras:
    tentativas -= 1

print('Errou')

print(f'Voce tem {tentativas}')

if tentativas == 0:
    print('Voce perdeu')
'''''


'''
import random

def get_word():

    with open('/Users/Admin/Desktop/words.txt', 'r') as f:

        words1 = f.read().splitlines()

    return random.choice(words1)

myword = get_word()

for i in myword:

    print('*', end=' ')

l = len(myword)
print('\nWord has %d letters' %l)

def check(myword, your_word, guess1):

    status = ''
    matches = 0

    for letter in myword:
        if letter in your_word:
            status += letter
        else:
            status += '*'
        if letter == guess1:
            matches += 1

    if matches > 1:
        print(matches, guess1)

    elif matches == 1:
        print(guess1)
    return status
def game():
    guess = 0
    guessed = False
    your_word = []
    turns = len(myword) + 1
    turns1 = turns

    print('Total turns: ', turns)
    while guess < turns1:
        guess1 = input("Digite seu palpite: ")

    turns -= 1

    print("Vire a esquerda", turns)

    if guess1 in your_word:
        print('Voce ja adivinhou')
    elif len(guess1) == 1:
        your_word.append(guess1)
        result = check(myword, your_word, guess1)
        if result == myword:
            guessed = True
            print("Voce ganhou " + name)
            print(myword)
        else:
            print(result)
    else:
        print("Invalid entry")
    guess += 1
    if guess == turns1:
        print("Word is:")
        print(myword)
game()
'''



def nearestMultiple(num):
    if num >= 4:
        near = num + (4 - (num % 4))
    else:
        near = 4

    return near

def lose1():
    print('\n\nVoce perdeu!')
    print('Mais sorte na proxima vez')
    exit(0)

def check(xyz):
    i = 1

    while i<len(xyz):
        if (xyz[i]-xyz[i-1])!= 1:
            return False
        i = i + 1
    return True

def start1():
    xyz = []
    last = 0

    while True:

        print('Digite "F" para arriscar pela primeira vez')
        print('Digite "S" para ter a segunda chance')
        chance = input('> ')

        if chance == 'F':
            while True:
                if last == 20:
                    lose1()
                else:
                    print   ('\nSua vez.')
                    print   ('\nQuantos números você deseja inserir?')
                    inp = int(input('> '))

                    if inp > 0 and inp <= 3:
                        comp = 4 - inp
                    else:
                        print('Entrada errada. Você foi desqualificado do jogo.')
                        lose1()
                        i, j = 1, 1
                    print("Now enter the values")

                    while i <= inp:
                        a = input('> ')
                        a = int(a)
                        xyz.append(a)
                        i = i + 1
                        last = xyz[-1]
                        if check(xyz) == True:
                            if last == 21:
                                lose1()
                            else:
                                while j <= comp:
                                    xyz.append(last + j)
                                    j = j + 1
                            print('Order of inputs after computer"s turn is:')
                            print(xyz)
                            last = xyz[-1]
                        else:
                            print('\nYou did not input consecutive integers.')
                            lose1()

        elif chance == 'S':
            comp = 1
            last = 0
            while last < 20:
                j = 1
                while j <= comp:
                    xyz.append(last + j)
                    j = j + 1
                print('Order of inputs after computer"s turn is:')
                print(xyz)

                if xyz[-1] == 20:
                    lose1()
                else:
                    print('\nYour turn.')
                    print('\nHow many numbers do you wish to enter?')
                    inp = input('> ')
                    inp = int(inp)
                    i = 1
                    print('Enter your values')
                    while i <= inp:
                        xyz.append(int(input('> ')))
                        i = i + 1
                    last = xyz[-1]

                    if check(xyz) == True:
                        near = nearestMultiple(last)
                        comp = near - last
                        if comp == 4:
                            comp = 3
                        else:
                            comp = comp
                    else:
                        print('\nYou did not input consecutive integers.')
                        lose1()
            print('\n\nCONGRATULATIONS !!!')
            print('YOU WON !')
            exit(0)
        else:
            print('wrong choice')

game = True
while game == True:
    print('Player 2 is computer.')
    print('Do you want to play the 21 number game? (Yes / No)')
    ans = input('> ')

    if ans == 'Yes':
        start1()
    else:
        print('Do you want quit the game? (yes / no)')
        nex = input('> ')

        if nex == 'yes':
            print('You are quitting the game...')
            exit(0)

        elif nex == 'no':
            print('Continuing...')
        else:
            print('Wrong choice')



'''
from tkinter import *

root = Tk()

root.title('By: Win')
root.geometry('350x200')

menu = Menu(root)
item = Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)


lbl = Label(root, text = 'Are you a Geek?')
lbl.grid()

txt = Entry(root, width=10)
txt.grid(column =1, row =0)

def clicked():

    res = 'You wrote' + txt.get()
    lbl.configure(text = res)


btn = Button(root, text = 'Click me',
             fg = 'red', command=clicked)
btn.grid(column=2, row=0)

root.mainloop()
'''


































































































