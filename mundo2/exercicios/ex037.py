print('=' * 43)
print('CALCULADORA DE CONVERSÃO DE BASES NUMÉRICAS')
print('=' * 43)

n = int(input('Insira um número inteiro: '))
print('Escolha uma das bases para conversão: ')
print('[1] BINÁRIO | [2] OCTAL | [3] HEXADECIMAL')
x = int(input('Insira a opção desejada: '))

if x == 1:
    print(f'{n} convertido para BINÁRIO = {bin(n)[2:]}')
elif x == 2:
    print(f'{n} convertido para OCTAL = {oct(n)[2:]}')
elif x == 3:
    print(f'{n} convertido para HEXADECIMAL = {hex(n)[2:]}')
else:
    print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE.')
