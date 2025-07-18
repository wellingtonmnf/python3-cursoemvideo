preco = float(input('Digite o preço do produto: '))
novopreco = preco - (preco * 5 / 100)
print('Preço com 5% de desconto: R$ {:.2f}'.format(novopreco))
