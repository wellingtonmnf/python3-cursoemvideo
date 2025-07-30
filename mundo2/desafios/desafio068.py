from random import randint

print('=-' * 15)
print(f'{"VAMOS JOGAR PAR OU ÍMPAR":^30}')
print('=-' * 15)

resultado = ''
vitorias = 0

while True:

    jogador = int(input('Diga um valor: '))
    escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    computador = randint(0, 9)
    soma = jogador + computador

    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'

    print('-' * 30)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU {resultado}')
    print('-' * 30)

    if escolha in 'IiÍí':
        escolha = 'Í'

    if escolha == resultado[0]:
        print('Você VENCEU!\nVamos jogar novamente...')
        print('=-' * 15)
        vitorias += 1
    else:
        print('Você PERDEU!')
        print('=-' * 15)
        print(f'GAME OVER! Você venceu {vitorias} vez(es).')
        break

print('-' * 30)

