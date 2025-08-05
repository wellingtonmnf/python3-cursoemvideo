# valores = [] # Cria uma lista vazia
valores = list()  # Cria uma lista vazia através do metodo 'list()'

valores.append(5)
valores.append(9)
valores.append(4)
# print(valores)

for v in valores:
    print(f'{v}...', end='')
print()
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
