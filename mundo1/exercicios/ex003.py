n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
soma = n1 + n2
print('A soma vale', soma)
print('A soma vale {}'.format(soma))
# Sintaxe normal
print('A soma entre', n1, '+', n2, 'é igual a', soma)
# Sintaxe com format()
print('A soma entre {} e {} é igual a {}'.format(n1, n2, soma))
# Sintaxe com f-string
print(f'A soma entre {n1} e {n2} é igual a {soma}')
