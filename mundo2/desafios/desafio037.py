print('-' * 30)
print('CONVERSOR DE NÚMEROS')
print('-' * 30)

n = int(input('Digite um número inteiro: '))
print('Escolha a base de conversão do número:')
print('1 - BINÁRIO | 2 - OCTAL | 3 - HEXADECIMAL')
opcao = int(input('Digite a opção: '))

if opcao == 1:
    print(f'O número {n} na base binária é igual a {bin(n)[2:]}')
elif opcao == 2:
    print(f'O número {n} na base octal é igual a {oct(n)[2:]}')
elif opcao == 3:
    print(f'O número {n} na base hexadecimal é igual a {hex(n)[2:].upper()}')
else:
    print('Opção inválida!')

