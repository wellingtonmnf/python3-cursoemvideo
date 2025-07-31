print('=' * 40)
print('{:^40}'.format('BANCO CEV'))
print('=' * 40)

divisor = cedulas = 0
valor = int(input('Que valor você quer sacar? R$ '))

while True:

    if valor >= 50:
        divisor = 50
    elif valor >= 20:
        divisor = 20
    elif valor >= 10:
        divisor = 10
    elif valor >= 1:
        divisor = 1

    if valor > 0:
        cedulas = valor // divisor
        print(f'Total de {cedulas:3} cédula(s) de R$ {divisor}')
        valor = valor % divisor

    if valor == 0:
        break

print('=' * 40)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
