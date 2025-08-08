estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado) # Ao colocar na lista, os valores do dicionário serão atualizados a cada volta do laço. Ao final, haverão 3 instâncias do objeto estado na lista, todas com o mesmo valor que foi atualizado

print(brasil)

for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado[:]) # Não é permitido fazer fatiamento em dicionários. Essa técnica não resolverá o problema

print(brasil)