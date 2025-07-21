n = str(input('Digite o nome completo: ')).strip()
nomes = n.split()

print(f'Primeiro nome: {nomes[0]} | Último sobrenome: {nomes[len(nomes)-1]}')
