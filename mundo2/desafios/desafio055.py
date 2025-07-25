print('-' * 40)
print(f'{"LEITOR DE PESO":~^40}')
print('-' * 40)

maior, menor = 0, 0

for c in range(1, 6):
    peso = float(input(f'Digite o peso (kg) da {c}ª pessoa: '))

    if menor == 0:
        menor = peso
    elif peso < menor:
        menor = peso

    if maior == 0:
        maior = peso
    elif peso > maior:
        maior = peso

print('-' * 40)
print(f'Maior peso: {maior:<.2f} kg')
print(f'Menor peso: {menor:<.2f} kg')
print('-' * 40)
