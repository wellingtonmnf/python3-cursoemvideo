from random import randint

seq = ()
for c in range(0,5):
    n = randint(0,9)
    nova = (n,)
    seq = seq + nova
print(f'Os valores sorteados foram: ',end='')
for num in seq:
    print(f'{num} ',end='')

for c in range(0,5):
    if c == 0:
        maior = menor = seq[c]
    else:
        if seq[c] > maior:
            maior = seq[c]
        if seq[c] < menor:
            menor = seq[c]

print(f'\nO maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
