def ficha(n=' ', g=' '):
    if len(n) == 0:
        n = '<desconhecido>'
    if len(g) == 0:
        g = 0
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')


print('-' * 30)
nome = str(input('Nome do jogador: ')).strip()
gols = str(input('Número de gols: ')).strip()
ficha(nome, gols)
