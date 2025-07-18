dias = int(input('Duração do aluguel (dias): '))
km = float(input('Quantos Km foram percorridos? '))
preco = (60 * dias) + (0.15 * km)
print(f'O preço do aluguel do carro é de R$ {preco:.2f}')
