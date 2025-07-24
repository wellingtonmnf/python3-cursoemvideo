peso = float(input('Digite o peso (kg): '))
altura = float(input('Digite a altura (m): '))
imc = peso / (altura * altura)

print(f'IMC = {imc:.1f} kg/m²')

if imc < 18.5:
    print('Resultado: ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('Resultado: PESO IDEAL')
elif 25 <= imc < 30:
    print('Resultado: SOBREPESO')
elif 30 <= imc < 40:
    print('Resultado: OBESIDADE')
else:
    print('Resultado: OBESIDADE MÓRBIDA')
