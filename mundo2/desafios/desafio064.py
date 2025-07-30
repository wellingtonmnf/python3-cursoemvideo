cont = soma = n = 0
while n != 999:
    n = int(input('Digite um número inteiro [999 = SAIR]: '))
    if n != 999:
        cont += 1
        soma += n
print(f'TOTAL DE NÚMEROS DIGITADOS: {cont}')
print(f'SOMA DOS NÚMEROS DIGITADOS: {soma}')
