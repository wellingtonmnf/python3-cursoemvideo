num1 = int(input('Insira o 1º número inteiro: '))
num2 = int(input('Insira o 2º número inteiro: '))

if num1 == num2:
    print(f'Os números possuem o mesmo valor. São iguais.')
elif num1 > num2:
    print(f'O PRIMEIRO número é maior.')
else:
    print(f'O SEGUNDO número é maior.')