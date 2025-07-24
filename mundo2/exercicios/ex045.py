from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('Suas opções: ')
print('''[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ!!!')
print('=-' * 20)
if jogador < 0 or jogador > 2:
    print('Opção inválida!')
else:
    print(f'Computador jogou: {itens[computador]}')
    print(f'Jogador jogou: {itens[jogador]}')

    if computador == 0: # Computador jogou PEDRA
        if jogador == 0:
            print('EMPATE')
        elif jogador == 1:
            print('JOGADOR VENCE')
        elif jogador == 2:
            print('COMPUTADOR VENCE')
        else:
            print('JOGADA INVÁLIDA!')
    elif computador == 1: # Computador jogou PAPEL
        if jogador == 0:
            print('COMPUTADOR VENCE')
        elif jogador == 1:
            print('EMPATE')
        elif jogador == 2:
            print('JOGADOR VENCE')
        else:
            print('JOGADA INVÁLIDA!')
    elif computador == 2: # Computador jogou TESOURA
        if jogador == 0:
            print('JOGADOR VENCE')
        elif jogador == 1:
            print('COMPUTADOR VENCE')
        elif jogador == 2:
            print('EMPATE')
        else:
            print('JOGADA INVÁLIDA!')

print('=-' * 20)
