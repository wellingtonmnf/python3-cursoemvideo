print('=' * 30)
print(f'{" BANCO CEV ":^30}')
print('=' * 30)
# Não usei 'while True:', por isso procurei fazer outra solução
valor = int(input('Que valor você quer sacar? R$ '))

cedula50 = cedula20 = cedula10 = cedula1 = 0

if valor // 50 > 0:
    cedula50 = valor // 50
    valor =  valor % 50
if valor // 20 > 0:
    cedula20 = valor // 20
    valor = valor % 20
if valor // 10 > 0:
    cedula10 = valor // 10
    valor = valor % 10
if valor // 1 > 0:
    cedula1 = valor // 1

print(f'Total de {cedula50:3} cédula(s) de R$ 50')
print(f'Total de {cedula20:3} cédula(s) de R$ 20')
print(f'Total de {cedula10:3} cédula(s) de R$ 10')
print(f'Total de {cedula1:3} cédula(s) de R$ 1')

print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
