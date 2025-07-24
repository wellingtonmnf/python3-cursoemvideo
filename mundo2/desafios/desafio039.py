from datetime import date

print('*'*30)
print('ALISTAMENTO MILITAR')
print('*'*30)

anonascimento = int(input('Informe o ano de nascimento: '))
anoatual = date.today().year

idade = anoatual - anonascimento
print(f'Você tem {idade} anos')

if idade < 18:
    print(f'Faltam {18 - idade} anos para o alistamento militar')
elif idade == 18:
    print('É hora de se alistar no serviço militar')
else:
    print(f'Tempo decorrido do prazo do alistamento: {idade - 18} ano(s)')