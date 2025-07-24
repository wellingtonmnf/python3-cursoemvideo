print('-' * 14)
print('MEDIDOR DE IMC')
print('-' * 14)

peso = float(input('Informe o peso (kg) da pessoa: '))
altura = float(input('Informe a altura (m) da pessoa: '))

imc = peso / (altura ** 2)

print(f'IMC = {imc:.2f} kg/m²')

if imc < 18.5:
    print('Status: ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('Status: PESO IDEAL')
elif 25 <= imc < 30:
    print('Status: SOBREPESO')
elif 30 <= imc <= 40:
    print('Status: OBESIDADE')
else:
    print('Status: OBESIDADE MÓRBIDA')
