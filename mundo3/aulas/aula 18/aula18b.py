teste = list() # Cria um objeto teste do tipo lista
teste.append('Gustavo') # Insere elemento no índice 0 de 'teste'
teste.append(40) # Insere elemento no índice 1 de 'teste'
print(teste) # Imprime a lista
galera = list() # Cria um novo objeto 'galera' do tipo lista
galera.append(teste[:]) # Cria UMA CÓPIA DO OBJETO 'TESTE' do tipo lista no índice 0 da nova lista
teste[0] = 'Maria' # Modifica o valor do índice 0 no objeto 'teste'
teste[1] = 22 # Modifica o valor do índice 1 no objeto 'teste'
galera.append(teste[:]) # CRIA UMA NOVA CÓPIA DO MESMO OBJETO 'teste' (mesma variável de referência do objeto QUE TEVE VALORES ALTERADOS) no índice 1 da nova lista
print(galera) # Imprime a nova lista
