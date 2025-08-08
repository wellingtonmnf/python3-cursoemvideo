pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas) # Imprime o dicionário
#print(pessoas[0]) # Gera um erro de chave, pois o dicionário não está definido por índices, e sim por chaves
print(pessoas['nome']) # Imprime o valor contido na chave nome
print(pessoas['idade']) # Imprime o valor contido na chave idade
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos') # Imprime os valores contidos nas chaves nome e idade
print(pessoas.keys()) # Imprime todas as chaves contidas no dicionário
print(pessoas.values()) # Imprime todos os valores contidas no dicionário
print(pessoas.items()) # Imprime todos os itens contidas no dicionário
