nomecompleto = str.strip(input('Digite o nome completo: '))
lista = nomecompleto.split()
primeironome = lista[0]
ultimonome = lista[len(lista) -1]
print(f'Primeiro nome: {primeironome}')
print(f'Último nome: {ultimonome}')