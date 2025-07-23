from random import randint

n = randint(0, 5)

print('Tente advinhar qual número o computador pensou!')
x = int(input('Escolha um número entre 0 e 5: '))
print(f'Número pensado pelo computador: {n}')

if x == n:
    print('Você acertou! Parabéns!')
else:
    print('Você errou! Que pena!')
