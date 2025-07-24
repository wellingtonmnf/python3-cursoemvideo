print('-' * 50)
print('ANÁLISE DE EMPRÉSTIMO')
print('-' * 50)

valorimovel = float(input('Insira o valor do imóvel (R$): '))
salario = float(input('Insira o salário do cliente (R$): '))
anos = int(input('Prazo do financiamento (anos): '))
prestacoes = valorimovel / (anos * 12)

print('-' * 50)
print('ANÁLISE: ')
print(f'Valor do imóvel: R$ {valorimovel:.2f}')
print(f'Nº de prestações: {anos * 12}x')
print(f'Valor do parcelamento: R$ {prestacoes:.2f}')
print(f'Limite da prestação: R$ {(salario * 30 / 100):.2f}')

print('-' * 50)
print('RESULTADO DA ANÁLISE: ', end='')
if prestacoes > (salario * 30 / 100):
    print('EMPRÉSTIMO NEGADO')
else:
    print('EMPRÉSTIMO APROVADO')
