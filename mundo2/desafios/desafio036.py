print('=' * 25)
print('APROVAÇÃO DE EMPRÉSTIMO')
print('=' * 25)

valorcasa = float(input('Digite o valor do imóvel (R$): '))
salario = float(input('Digite o valor do salário (R$): '))
anos = int(input('Digite o prazo do financiamento desejado (anos): '))

prestacoes = valorcasa / (anos * 12)

if prestacoes > (salario * 30 / 100):
    print(
        'Seu empréstimo \033[7;31mnão\033[m pode ser aprovado. \nO valor das parcelas do financiamento não é financeiramente saudável.')
else:
    print(f'Seu empréstimo foi aprovado! \033[7;34mPARABÉNS!\033[m')
    print(f'Valor do imóvel: R$ {valorcasa:.2f}')
    print(f'Parcelamento: {(anos * 12)} prestações de R$ {prestacoes:.2f}')
