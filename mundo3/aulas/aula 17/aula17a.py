num = [2, 5, 9, 1]
num[2] = 3  # Diferente das tuplas, listas são estruturas mutáveis
# num[4] = 7 # Não é possível adicionar elementos atribuindo a indices inexistentes
num.append(7) # O metodo append adiciona um elmento ao final da lista
num.sort() # Ordena a lista em ordem crescente/alfabética
num.sort(reverse=True) # Ordena a lista em ordem decrescente/alfabética
num.insert(2,0) # Insere no INDICE 2 o VALOR 0
num.pop() # Elimina o último valor da lista (era o número '1')
num.pop(2) # Elimina o valor no índice 2 da lista
print(num)
print(f'Essa lista tem {len(num)} elementos') # Comprimento da lista
