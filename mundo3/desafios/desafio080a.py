valores = []
for c in range(0, 5):

    n = int(input('Digite um valor: '))

    if c == 0:
        valores.append(n)
        print('Adicionado ao final da lista...')
    else:
        for pos, valor in enumerate(valores):
            if n < valor:
                valores.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista')
                break
            if n > valores[-1]:
                valores.append(n)
                print('Adicionado ao final da lista...')
print('-=' * 30)
print(valores)
