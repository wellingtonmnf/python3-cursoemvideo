a = [2, 3, 4, 7]
b = a
b[2] = 8 # mudança na lista original (variável de referência? Provavelmente, sim)
c = a[:] # Cria uma COPIA dos valores em uma variável nova (outro objeto? Provavelmente, sim)
c[2] = 5
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista C: {c}')
