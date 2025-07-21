n = str.strip(input('Digite um número entre 0 e 9999: '))
num = list(n)
num.reverse()

print(f'Unidade: {num[0:1]}')
print(f'Dezena:  {num[1:2]}')
print(f'Centena: {num[2:3]}')
print(f'Milhar:  {num[3:]}')
