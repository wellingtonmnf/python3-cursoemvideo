num = [2, 5, 9, 1]
num[2] = 3  # Diferente das tuplas, listas são estruturas mutáveis
num.append(7) # O metodo append adiciona um elmento ao final da lista
num.sort(reverse=True) # Ordena a lista em ordem decrescente/alfabética
num.insert(2,2) # Insere no INDICE 2 o VALOR 2
num.remove(2) # Remove o PRIMEIRO VALOR ENCONTRADO passado como parâmetro
if 4 in num:
    num.remove(4) # Se o valor não existir na lista, retorna exceção
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos') # Comprimento da lista
