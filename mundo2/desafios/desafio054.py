from datetime import date

print('-' * 36)
print(f'{"CHECADOR DE MAIORIDADE":^36}')
print('-' * 36)

data = date.today().year
nasc, menor, maior = 0, 0, 0

for c in range(0, 7):
    nasc = int(input('Insira o ano de nascimento: '))
    if (data - nasc) < 21:
        menor += 1
    else:
        maior += 1

print(f'Nº de pessoas maiores de idade: {maior}')
print(f'Nº de pessoas menores de idade: {menor}')
