time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: ')).strip().capitalize()
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break
print('-=' * 50)
print(' COD ', end='')
for i in jogador.keys():
    print(f'{i.upper():<15}', end='')
print()
print('-' * 50)
for k, v in enumerate(time):
    print(f'{k:^5}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 50)
while True:
    num = int(input('Mostrar dados de qual jogador? [999 => SAIR]: '))
    print('-=' * 50)
    if num == 999:
        break
    elif num < len(time):
        print(f'LEVANTAMENTO DO JOGADOR: {time[num]['nome']}')
        print(f'O jogador {time[num]['nome']} jogou {len(time[num]["gols"])} partidas')
        for pos, g in enumerate(time[num]["gols"]):
            print(f'=> Na partida {pos}, fez {g} gols.')
        print(f'Foi um total de {time[num]["total"]} gols')
    else:
        print('ERRO! JOGADOR NÃO ENCONTRADO NA BASE DE DADOS')
    print('-' * 40)
print('FINALIZANDO...')
print('VOLTE SEMPRE!'.center(50,'-'))
