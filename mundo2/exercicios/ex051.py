print('=' * 30)
print(f'{"10 TERMOS DE UMA PA":^30}')
print('=' * 30)

primeirotermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

# Fórmula para calcular um termo de uma PA: a_n =a_1 + (n − 1) × r
# Fórmula para calcular um termo de uma PA: aₙ =a₁ + (n − 1) × r

decimo = primeirotermo + (10 - 1) * razao  # Essa fórmula calcula o décimo termo de uma PA
# A linha abaixo calcula o 11º termo da PA para usar somente o valor da variável na função range, que tme seu 2º parâmetro excludente
decimoprimeiro = primeirotermo + (11 - 1) * razao  # Essa fórmula calcula o décimo primeiro termo de uma PA

for c in range(primeirotermo, decimo + razao, razao):  # O limite é achado através da fórmula
    print(c, end=' ➞ ')
print('ACABOU')

for c in range(primeirotermo, decimoprimeiro, razao):
    print(c, end=' ➞ ')
print('ACABOU')
