print('+'*20)
print('CALCULADORA DE PREÇO')
print('+'*20)

preconormal = float(input('Digite o preço do produto (R$): '))
print('Escolha a condição de pagamento:')
print('1 - DINHEIRO/CHEQUE | 2 - CARTÃO (1X) | 3 - CARTÃO (2X) | 4 - CARTÃO (3X OU +)')

condicao = int(input('Digite a opção desejada: '))

if condicao == 1:
    print(f'VALOR FINAL: R$ {preconormal - (preconormal*10/100):.2f} | DESCONTO: 10%')
elif condicao == 2:
    print(f'VALOR FINAL: R$ {preconormal - (preconormal*5/100):.2f} | DESCONTO: 5%')
elif condicao == 3:
    print(f'VALOR FINAL: R$ {preconormal:.2f} | DESCONTO: 0%')
elif condicao == 4:
    print(f'VALOR FINAL: R$ {preconormal + (preconormal*20/100):.2f} | JUROS: 10%')
else:
    print('OPÇÃO INVÁLIDA!')


