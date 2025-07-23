print('Condição de existência de um triângulo')
l1 = float(input('Digite o valor do 1º lado (L1): '))
l2 = float(input('Digite o valor do 2º lado (L2): '))
l3 = float(input('Digite o valor do 3º lado (L3): '))

if (l1 < l2 + l3) and (l2 < l1 + l3) and (l3 < l1 + l2):
    print(f'É possível formar um triângulo? R: \033[30;42mSIM\033[m')
else:
    print(f'É possível formar um triângulo? R: \033[7;31mNÃO\033[m')