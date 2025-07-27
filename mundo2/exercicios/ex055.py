maior, menor = 0, 0

for pessoa in range(1, 6):
    peso = float(input(f'Peso da {pessoa}ª pessoa: '))

    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
           maior = peso
        if peso < menor:
           menor = peso

print(f'O maior peso lido foi de {maior:.2f} kg')
print(f'O menor peso lido foi de {menor:.2f} kg')
