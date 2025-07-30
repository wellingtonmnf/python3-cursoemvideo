from random import randint

print('Sou seu computador...')
computador = randint(0,10)
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if computador == jogador:
        acertou = True
    else:
        if computador > jogador:
            print('Mais... Tente mais uma vez.')
        elif computador < jogador:
            print('Menos... Tente mais uma vez.')
print(f'Acertou com {palpites} tentativas. Parabéns!')