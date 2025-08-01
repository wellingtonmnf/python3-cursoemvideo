variacoes = ('um', 'outro', 'mais um', 'o último')

numeros = ()
pares = ''
for c in range(0, 4):
    n = int(input(f'Digite {variacoes[c]} valor: (0->9) '))
    numeros += (n,)
print(f'Você digitou os valores: ', end='')

for numero in numeros:

    print(numero, end='')

    if numero % 2 == 0:
        pares += str(numero) + ' '

print(f'\nO valor 9 apareceu {numeros.count(9)} vez(es)')

if numeros.count(3) != 0:
    print(f'O valor 3 apareceu na {(numeros.index(3)) + 1} posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

print(f'Os valores pares digitados foram: {pares}')
