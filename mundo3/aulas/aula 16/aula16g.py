a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b # concatena os valores na ordem de a e b em uma nova tupla
print(len(c))
print(c)
print(c.count(5)) # Quantas vezes aparece '5' dentro da tupla 'c'
print(c.count(9))
print(c.index(8)) # Posição de '8' na tupla
print(c.index(2)) # Posição de '2' na tupla (se repetido, onde for encontrado primeiro)
print(c.index(2,3)) # Posição de '2' na tupla, contando a partir da posição 3

