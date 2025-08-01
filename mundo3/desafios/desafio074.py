from random import randint

seq = ''
for c in range(0,5):
    n = randint(0,9)
    seq += str(n)
# print(seq)
numeros = (int(seq[-5]), int(seq[-4]), int(seq[-3]), int(seq[-2]), int(seq[-1]))
print(f'Os valores sorteados foram: ',end='')
for n in numeros:
    print(f'{n} ',end='')

for c in range(0,5):
    if c == 0:
        maior = menor = numeros[c]
    else:
        if numeros[c] > maior:
            maior = numeros[c]
        if numeros[c] < menor:
            menor = numeros[c]

print(f'\nO maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
