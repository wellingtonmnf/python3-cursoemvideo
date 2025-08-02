variacoes = ('um', 'outro', 'mais um', 'o último')
seq = pares = ''
noves = 0
for c in range(0, 4):
    n = int(input(f'Digite {variacoes[c]} valor: (0->9) '))
    seq += str(n)
# print(seq)
numeros = (int(seq[-4]), int(seq[-3]), int(seq[-2]), int(seq[-1]))
print(f'Você digitou os valores {numeros}')

for numero in numeros:
    if numero == 9:
        noves += 1

    if numero % 2 == 0:
        pares += str(numero) + ' '

print(f'O valor 9 apareceu {noves} vez(es)')

if '3' in seq:
    print(f'O valor 3 apareceu na {(numeros.index(3)) + 1} posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

print(f'Os valores pares digitados foram: {pares}')
