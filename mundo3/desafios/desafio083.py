expressao = str(input('Digite a expressão: ')).strip().lower()

par1 = par2 = 0

for char in expressao:
    if char == '(':
        par1 += 1
    if char == ')':
        par2 += 1

print(f"Parênteses de abertura: {par1}")
print(f"Parênteses de fechamento: {par2}")

if par1 == par2:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
