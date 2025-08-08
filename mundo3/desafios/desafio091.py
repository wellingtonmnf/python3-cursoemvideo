from random import randint
from time import sleep

jogadores = dict()
datatemp = []
# Sorteando os números e guardando os dados em um dicionário
for c in range(1, 5):
    num = randint(1, 6)
    jogadores[f'jogador {c}'] = num
# Lendo os resultados de cada jogador no dicionário
print('Valores sorteados:')
for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(1)
# Montando uma lista com jogadores e numeros em formato de tuplas
for item in jogadores.items():
    datatemp.append(item)
# Ordenando manualmente a posição das tuplas na lista comparando o valor de cada chave
for c in range(0,4):
    for i in range(0,4):
        if datatemp[c][1] > datatemp[i][1]:
            swap = datatemp[i]
            datatemp[i] = datatemp[c]
            datatemp[c] = swap
# Adicionando os valores ordenados da lista em um novo dicionário
ordenados = {}
for j in datatemp:
    ordenados[j[0]] = j[1]
# Imprimindo os valores ordenados
print('Ranking dos jogadores:')
cont = 0
for k,v in ordenados.items():
    cont += 1
    print(f'{cont}º lugar: {k} com {v}')
    sleep(1)
print('-' * 30)
