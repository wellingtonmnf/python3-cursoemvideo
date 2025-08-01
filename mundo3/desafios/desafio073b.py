brasileirao2017 = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco da Gama',
                   'Chapecoense', 'Atlético-MG', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport',
                   'Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print('Primeiros 5 colocados do Brasileirão 2025:')
print(brasileirao2017[:5])
print('-' * 20)

print('Últimos 4 colocados do Brasileirão 2025:')
print(brasileirao2017[16:])
print('-' * 20)

print('Lista de times em ordem alfabética')
print(sorted(brasileirao2017))
print('-' * 20)

for c in range(0,20):
    if brasileirao2017[c] == 'Chapecoense':
        print(f'A {brasileirao2017[c]} está na {c + 1}ª posição do campeonato')
