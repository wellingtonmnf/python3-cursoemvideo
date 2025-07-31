from random import randint

print('=-' * 15)
print(f'VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)

resultado = ''
vitorias = 0

while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PIÍ':
        tipo = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    print('-' * 30)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    print('-' * 30)
    if tipo == 'P':
        if total % 2 == 0:
            vitorias += 1
            print('Você VENCEU!')
        else:
            print('Você PERDEU!')
            break
    elif tipo in 'IÍ':
        if total % 2 == 1:
            vitorias += 1
            print('Você VENCEU!')
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {vitorias} vez(es).')
