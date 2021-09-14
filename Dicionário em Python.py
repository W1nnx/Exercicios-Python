dict = dict()

dict['nomes'] = str(input('Nome: '))
dict['medias'] = float(input(f'Media de {dict["nomes"]}: '))

rpr = ' '

print('-='*15)
print(f'  -  nome e igual a {dict["nomes"]}')
print(f'  -  média e igual a {dict["medias"]}')

if dict["medias"] >= 7.0:
    rpr = 'Aprovado'

elif dict["medias"] < 7.0 and dict["medias"] == 4.0:
    rpr = 'Recuperação'
else:
    rpr = 'Reprovado'

print(f'  -  situaçao e igual a {rpr}')