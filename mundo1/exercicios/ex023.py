num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print(f'Unidade: {u}')
print(f'Dezena: {d:>2}')
print(f'Centena: {c}')
print(f'Milhar: {m:>2}')
