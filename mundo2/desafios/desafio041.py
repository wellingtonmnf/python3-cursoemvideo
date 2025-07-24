from datetime import date

print('~' * 20)
print('CLASSIFICAÇÃO DA CNN')
print('~' * 20)

nasc = int(input('Informe o ano de nascimento do(a) atleta: '))
anoatual = date.today().year
idade = anoatual - nasc

print(f'Idade do(a) atleta: {idade} anos')

if idade <= 9:
    print('Categoria: MIRIM')
elif 9 < idade <= 14:
    print('Categoria: INFANTIL')
elif 14 < idade <= 19:
    print('Categoria: JÚNIOR')
elif 19 < idade <= 25:
    print('Categoria: SENIOR')
else:
    print('Categoria: MASTER')
