temp = []
princ = []
mai = men = 0

while True:
    temp.append(str(input('Nome: ')).strip().capitalize())
    temp.append(float(input('Peso (kg): ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()

    while True:
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resp not in 'SN':
            print('Tente novamente.', end=' ')
        else:
            break
    if resp == 'N':
        break

print('-=' * 30)
print(f'Ao todo você cadastrou {len(princ)} pessoas')
print(f'O maior peso foi de {mai:.2f} kg. Peso de: ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men:.2f} kg. Peso de: ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()
