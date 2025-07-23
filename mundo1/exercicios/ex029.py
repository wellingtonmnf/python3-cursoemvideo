from time import sleep

print('*'*30)
print('RADAR DA TRANSALVADOR')
print('*'*30)

velocidade = float(input('Qual a velocidade atual do veículo (km/h)? '))

if velocidade > 80.0:
    print('Veículo MULTADO! Excedeu a velocidade permitida | 80 Km/h')
    print('Calculando valor da multa...')
    sleep(2)
    print(f'Valor da multa: R$ {((velocidade-80)*7):.2f}')

print('Tenha um bom dia! Dirija com segurança!')