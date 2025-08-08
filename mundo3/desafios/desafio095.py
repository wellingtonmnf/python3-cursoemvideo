jogadores = []

while True:
    print('-' * 50)
    nome = str(input('Nome do jogador: ')).strip().capitalize()
    partidas = int(input(f'Quantas partidas {nome} jogou? '))
    gols_partida = []

    for c in range(0, partidas):
        gols_partida.append(int(input(f'Quantos gols na partida {c}? ')))

    total_gols = 0
    for gols in gols_partida:
        total_gols += gols

    jogador = {'nome': nome, 'partidas': partidas, 'gols por partida': gols_partida, 'total de gols': total_gols}

    jogadores.append(jogador)

    while True:
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resp not in 'SN':
            print('Tente novamente.', end=' ')
        else:
            break
    if resp == 'N':
        break

print('-' * 50)
print(f'{"COD":<5}{"NOME":<15}{"GOLS":<25}{"TOTAL":>5}')
print('-' * 50)
for pos, j in enumerate(jogadores):
    print(f'{pos:^5}{j["nome"]:<15}{str(j["gols por partida"]):<25}{j["total de gols"]:^5}')

while True:
    print('-' * 50)
    num = int(input('Mostrar dados de qual jogador? (999 PARA SAIR): '))

    if num == 999:
        print('FINALIZANDO...')
        break
    elif num < len(jogadores):
        print(f'LEVANTAMENTO DO JOGADOR: {jogadores[num]['nome']}')
        print(f'O jogador {jogadores[num]['nome']} jogou {jogadores[num]['partidas']} partidas')
        for pos, g in enumerate(jogadores[num]['gols por partida']):
            print(f'=> Na partida {pos}, fez {g} gols.')
        print(f'Foi um total de {jogadores[num]['total de gols']} gols')
    else:
        print('JOGADOR NÃO ENCONTRADO NA BASE DE DADOS')

print('VOLTE SEMPRE!'.center(50,'-'))
