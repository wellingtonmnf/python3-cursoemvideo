estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) # Agora, com as cópias feitas, a lista será preenchida com novos valores que foram atualziados durante o laço. O dicionário ficará com o último valor atualizado
print('-'*30)
print(brasil) # Imprime o valor de cada item na lista, no caso um dicionário
print(estado) # Imprime o valor atual do dicionário
print('-'*30)
for est in brasil:
    print(est) # Imprime o valor de cada item na lista, no caso um dicionário
print('-'*30)
for e in brasil:
    for k,v in e.items():
        print(f'O campo {k} tem valor {v}') # Imprime a chave e o valor de cada item na lista, no caso um dicionário
print('-'*30)
for e in brasil:
    for v in e.values():
        print(v, end=' ') # Imprime o valor de cada item na lista, no caso um dicionário
    print()
