# Diferente do que ocorre em outras linguagens de programação, como Java,
# uma tupla pode possuir dados de tipos diferentes em Python
pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)
del(pessoa) # O comando 'del' apaga da memória qualquer coisa no Python
del(pessoa[0]) # Não é possível deletar um item de uma tupla (tuplas são imutáveis)
print(pessoa) # Comando da erro por conta da deleção da tupla
