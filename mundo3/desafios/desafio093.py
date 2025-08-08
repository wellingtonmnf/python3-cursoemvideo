nome = str(input('Nome do jogador: ')).strip().capitalize()
partidas = int(input(f'Quantas partidas {nome} jogou? '))
qt_gols_partida = []

for c in range(0, partidas):
    qt_gols_partida.append(int(input(f'Quantos gols na partida {c}? ')))

total_gols = 0

for gols in qt_gols_partida:
    total_gols += gols
print('-' * 50)
jogador = {'nome': nome, 'partidas': partidas, 'gols por partida': qt_gols_partida, 'total de gols': total_gols}
print(jogador)
print('-' * 50)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-' * 50)
print(f'O jogador {nome} jogou {partidas} partidas')
for pos, g in enumerate(qt_gols_partida):
    print(f'=> Na partida {pos}, fez {g} gols.')
print(f'Foi um total de {total_gols} gols')
