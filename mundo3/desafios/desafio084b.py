pessoas = []
datatemp = []
maispesados = []
menospesados = []

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

pesos = []
for pes in pessoas:
    pesos.append(pes[1])

maiorpeso = max(pesos)
menorpeso = min(pesos)

for pessoa in pessoas:
    if pessoa[1] == maiorpeso:
        maispesados.append(pessoa[0])
    if pessoa[1] == menorpeso:
        menospesados.append(pessoa[0])

print('-' * 30)
print('RELATÓRIO')
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso foi de {maiorpeso:.2f} kg. Peso de: {maispesados}')
print(f'O menor peso foi de {menorpeso:.2f} kg. Peso de: {menospesados}')
