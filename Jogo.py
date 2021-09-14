import random

itensInv = []
itens = dict()

coletaItens = input('Voce quer pegar itens para o craft? (S/N) ')

if coletaItens == 'S':
    madeira = input('Qual item? ')
    if madeira == 'Madeira':
        itensInv.append('Madeira')
        coletaItens = input('Quantas madeiras voce quer? ')
        if coletaItens == 1:
            m = 1
        if coletaItens == 2:
            m = 2
            itensInv.append(m)

craft = input('Oque voce quer craftar? ')


if craft == 'Picareta de madeira':
    if itensInv[0] == madeira:
        print()
        print('Voce craftou uma picareta de madeira')




























































































