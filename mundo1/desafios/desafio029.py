v = float(input('Digite a velocidade do carro (km/h): '))

if v > 80:
    print('O carro foi multado por excesso de velocidade.')
    print(f'Valor da multa: R$ {((v-80)*7):.2f}')
