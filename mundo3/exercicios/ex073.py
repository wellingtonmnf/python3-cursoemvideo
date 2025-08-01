times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco da Gama',
                   'Chapecoense', 'Atlético-MG', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport',
                   'Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print('-=' * 15)
print(f'Lista de times do Brasileirão 2017: {times}')
print('-=' * 15)
print(f'Os 5 primeiros foram: {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos foram: {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'A Chapecoense ficou na {times.index("Chapecoense") + 1}ª posição')
print('-=' * 15)
