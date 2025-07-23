from random import randint
from time import sleep

print('-'*80)
print('Estou pensando em um número entre 0 e 5. Tente adivinhar qual...')
print('-'*80)

computador = randint(0,5) # Faz o programa escolher um número aleatório entre 0 e 5
jogador = int(input('Escolha um número entre 0 e 5: ')) # Usuário insere número para adivinhar
print('PROCESSANDO...')
sleep(1.5)

if jogador == computador:
    print(f'Número pensado: {computador} ... Você venceu! PARABÉNS!')
else:
    print(f'Número pensado: {computador} ... Você perdeu! QUE PENA!')
