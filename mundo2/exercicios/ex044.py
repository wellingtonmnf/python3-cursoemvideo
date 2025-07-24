print(f'{' LOJAS GUANABARA ':=^40}')

precocheio = float(input('Insira o valor total da compra (R$): '))

print("""FORMAS DE PAGAMENTO:
[1] - À VISTA | DINHEIRO/CHEQUE
[2] - À VISTA | CARTÃO 
[3] - 2X | CARTÃO 
[4] - 3X OU + | CARTÃO """)
x = int(input('Escolha a opção de pagamento: '))

if x == 1:
    total = precocheio - (precocheio * 10 / 100)
elif x == 2:
    total = precocheio - (precocheio * 5 / 100)
elif x == 3:
    total = precocheio
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R$ {parcela:.2f} SEM JUROS')
elif x == 4:
    total = precocheio + (precocheio * 20 / 100)
    totparcelas = int(input('Insira o nº de parcelas: '))
    parcela = total / totparcelas
    print(f'Sua compra será parcelada em {totparcelas}x de R$ {parcela:.2f} COM JUROS')
else:
    total = precocheio
    print('Opção de pagamento inválida! Tente novamente.')

print(f'Valor da compra: R$ {precocheio:.2f} | Valor final: R$ {total:.2f}')
