import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {p:.2f} é igual a {moeda.metade(p, True)}')
print(f'O dobro de R$ {p:.2f} é igual a {moeda.dobro(p, False)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p,10, False)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}')
