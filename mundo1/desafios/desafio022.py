nome = str.strip(input('Digite o nome completo: '))
lista = nome.split()
nome1 = lista[0]
nomecompleto = nome.replace(' ','')
print(f'Nome em MAIÚSCULO: {nome.upper()}')
print('Nome em minúsculo: {}'.format(nome.lower()))
print(f'Total de letras do nome completo: {len(nomecompleto)}')
print(f'Total de letras do primeiro nome: {len(nome1)}')

