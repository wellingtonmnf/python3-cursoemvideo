from datetime import date

nascimento = int(input('Insira o ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - nascimento

print(f'Os nascidos em {nascimento} possuem hoje {idade} anos.')

if idade == 18:
    print(f'Deveriam se alistar este ano')
elif idade < 18:
    print(f'Deverá se alistar daqui a {18 - idade} ano(s)')
else:
    print(f'Deveriam ter se alistado há {idade - 18} ano(s)')

print(f'Ano do alistamento: {nascimento + 18}')
