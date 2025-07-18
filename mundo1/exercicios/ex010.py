real = float(input('Quanto você tem na carteira? R$ '))
dolar = float(input('Qual a cotação do dólar hoje? US$ '))
euro = float(input('Qual a cotação do euro hoje? € '))
print('Com R$ {:.2f} você pode comprar:\n US$ {:.2f}\n €   {:.2f}'.format(real, (real / dolar), (real / euro)))
