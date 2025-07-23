n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2) / 2
print(f'A média é igual a {m:.1f}')
# Condição composta
if m >= 6.0:
    print('Sua média foi boa. PARABÉNS!')
else:
    print('Sua média foi ruim. ESTUDE MAIS!')

print('FIM')
