termo = int(input('Digite o 1º termo da PA: '))
razao = int(input('Digite a razão da PA: '))
c = 1

while c <= 10:
    print(termo, end=' ➞ ')
    termo += razao
    c += 1
print('FIM')
