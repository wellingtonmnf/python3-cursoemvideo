pessoas = []
datatemp = []
maispesados = []
menospesados = []
maiorpeso = menorpeso = 0

print(f'{" CADASTRO DE PESSOAS ":*^40}')
while True:

    nome = str(input('Nome: ')).strip().upper()
    peso = float(input('Peso (Kg): '))
    datatemp.append(nome)
    datatemp.append(peso)
    pessoas.append(datatemp[:])
    datatemp.clear()

    while True:
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resp not in 'SN':
            print('Tente novamente.', end=' ')
        else:
            break
    if resp == 'N':
        break

for pos, pessoa in enumerate(pessoas):
    if pos == 0:
        maiorpeso = menorpeso = pessoa[1]
    else:
        if pessoa[1] > maiorpeso:
            maiorpeso = pessoa[1]
        if pessoa[1] < menorpeso:
            menorpeso = pessoa[1]

for pessoa in pessoas:
    if pessoa[1] == maiorpeso:
        maispesados.append(pessoa[0])
    if pessoa[1] == menorpeso:
        menospesados.append(pessoa[0])

print('-' * 30)
print('RELATÓRIO')
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso foi de {maiorpeso}. Peso de {maispesados}')
print(f'O menor peso foi de {menorpeso}. Peso de {menospesados}')
