brasil = [] # Cria uma lista
estado1 = {'uf': 'Rio de Janeiro', 'sigla':'RJ'} # Cria um dicionário
estado2 = {'uf': 'São Paulo', 'sigla':'SP'} # Cria um dicionário
brasil.append(estado1) # Adiciona o 1º dicionário a lista
brasil.append(estado2) # Adiciona o 1º dicionário a lista
print(estado1) # Imprime o 1º dicionário
print(estado2) # Imprime o 2º dicionário
print(brasil) # Imprime a lista
print(brasil[0]) # Imprime o 1º elemento da lista (dicionário 1)
print(brasil[1]) # Imprime o 1º elemento da lista (dicionário 1)
print(brasil[0]['uf']) # Imprime o valor da chave 'uf' no 1º elemento da lista (dicionário 1)
print(brasil[1]['sigla']) # Imprime o valor da chave 'sigla' no 2º elemento da lista (dicionário 2)