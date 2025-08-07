from random import randint
from time import sleep

jogos = []
datatemp = []

print('-' * 30)
print('JOGA NA MEGA-SENA'.center(30))
print('-' * 30)

numero_jogos = int(input('Quantos jogos você deseja fazer? '))

for cont in range(0, numero_jogos):
    while len(datatemp) < 6:

        num = randint(1, 60)

        if num not in datatemp:
            datatemp.append(num)

    if len(datatemp) == 6:
        datatemp.sort()
        jogos.append(datatemp[:])
        datatemp.clear()

print(f' SORTEANDO {numero_jogos} JOGOS '.center(30, '='))
for pos, jogo in enumerate(jogos):
    sleep(1)
    print(f'Jogo {pos + 1}: ', end='')
    for n in jogo:
        print(f'{n:02}', end=' ')
    print()
    print('-' * 30)
print(f' BOA SORTE! '.center(30, '='))
