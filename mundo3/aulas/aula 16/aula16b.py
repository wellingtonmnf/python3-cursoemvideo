lanches = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim') # tupla
print(lanches[1])
print(lanches[3])
print(lanches[-2]) # Número negativo volta iniciando pelo último índice. A contagem começa pelo 1, e não pelo 0
print(lanches[1:3]) # Com fatiamento, 1º índice é includente e o 2º é excludente
print(lanches[2:]) # Com fatiamento, 1º índice é includente e falta do 2º varre a coleção até o final
print(lanches[:2]) # Com fatiamento, falta do 1º índice varre a coleção desde o início e o 2º é excludente
print(lanches[-2:]) # Número negativo no 1º índice volta contagem da posição iniciando pelo último índice e falta do 2º varre a coleção até o final
print(lanches[-3:]) # Número negativo no 1º índice volta contagem da posição iniciando pelo último índice e falta do 2º varre a coleção até o final
print(lanches) # imprime toda a coleção
