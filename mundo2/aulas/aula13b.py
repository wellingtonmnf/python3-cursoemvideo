n = int(input('Digite um número: '))

for c in range(0, n):
    print(c)
print('FIM')
print('-' * 10)
for c in range(0, n + 1):
    print(c)
print('FIM')
print('+' * 30)
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')
print('+' * 30)
for c in range(0,3):
    n = int(input('Digite um número: '))
print('FIM')
print('+' * 30)
s = 0
for c in range(0,3):
    n = int(input('Digite um número: '))
    s += n
print(f'O somatório de todos os valores foi {s}')
print('FIM')
