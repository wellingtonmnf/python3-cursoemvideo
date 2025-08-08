pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
pessoas['nome'] = 'Leandro' # Muda o valor dentro da chave 'nome'
pessoas['peso'] = 98.5 # Adiciona um novo par de chave-valor ao dicionário
del pessoas['sexo'] # Deleta uma chave, juntamente com seus valores em um dicionário
for k,v in pessoas.items():
    print(f'{k} = {v}')
