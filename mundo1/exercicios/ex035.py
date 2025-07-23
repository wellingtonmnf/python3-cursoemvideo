print('^' * 30)
print('Analisador de triângulos')
print('^' * 30)

a = float(input('Lado A: '))
b = float(input('Lado B: '))
c = float(input('Lado C: '))

if a < b + c and b < a+c and c < a+b:
    print('Essas medidas podem formar um triângulo')
else:
    print('Essas medidas NÃO podem formar um triângulo')
