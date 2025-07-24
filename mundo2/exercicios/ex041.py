from datetime import date

nascimento = int(input('Digite o ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - nascimento

print(f'O atleta possui {idade} anos')

if idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: JÚNIOR')
elif idade <= 25:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')
