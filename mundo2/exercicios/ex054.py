from datetime import date

anoatual = date.today().year
menores, maiores = 0, 0

for pessoa in range(1, 8):
    nasc = int(input(f'Em que ano a {pessoa}ª pessoa nasceu? '))

    idade = anoatual - nasc

    if idade < 21:
        menores += 1
    else:
        maiores += 1

print(f'Ao todo tivemos {maiores} pessoas maiores de idade')
print(f'E também tivemos {menores} pessoas menores de idade')
