pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# Este laço mostra todas as chaves do dicionário
for k in pessoas:
    print(k)
# Este laço mostra todas as chaves do dicionário
for k in pessoas.keys():
    print(k)
# Este laço mostra todos os valores do dicionário
for v in pessoas.values():
    print(v)
# Este laço mostra todos os itens do dicionário
for i in pessoas.items():
    print(i)
# Este laço mostra todos os itens do dicionário
for k,v in pessoas.items():
    print(f'{k} = {v}')
