from time import sleep

distancia = float(input('Digite a distância do percurso da viagem (km): '))
print(f'Distância da viagem: {distancia} km')
print('Caculando o valor da passagem...')
sleep(2)
print(f'Valor da passagem: R$ {(distancia*0.5):.2f}' if distancia <= 200 else f'Valor da passagem: R$ {(distancia*0.45):.2f}' )