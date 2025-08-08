jogador = dict()
gols = list()
soma = 0
jogador['nome'] = str(input('Nome do Jogador: '))
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, jogador['partidas']):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
jogador['gols'] = gols
for g in gols:
    soma += g
jogador['total'] = soma
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f' O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
for pos, g in enumerate(gols):
    print(f'  => Na partida {pos}, fez {g} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
