brasileirao2017 = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco da Gama',
                   'Chapecoense', 'Atlético-MG', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport',
                   'Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print('Primeiros 5 colocados do Brasileirão 2025:')
for c in range(0, 5):
    print(f'{c + 1}º - {brasileirao2017[c]}')
print('-' * 20)

print('Últimos 4 colocados do Brasileirão 2025:')
for c in range(16, 20):
    print(f'{c + 1}º - {brasileirao2017[c]}')
print('-' * 20)

print('Lista de times em ordem alfabética')
# print(sorted(brasileirao2017))
alfabetica = sorted(brasileirao2017)  # nova tupla com ordenação, pois tuplas são imutáveis
for time in alfabetica:
    print(time)
print('-' * 20)

for pos, time in enumerate(brasileirao2017):
    if time == 'Chapecoense':
        print(f'A {time} está na {pos + 1}ª posição do campeonato')
