import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {p:.2f} é igual a {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de R$ {p:.2f} é igual a {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p,10))}')
print(f'Reduzindo 13%, temos {moeda.moeda(moeda.diminuir(p, 13))}')
