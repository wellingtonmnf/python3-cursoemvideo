# Ordenar primeiro por nota, depois por idade
vendas = [
    ('João', 25, 1000),
    ('Maria', 30, 1000),  # Mesma venda que João
    ('Pedro', 22, 1500),
    ('Joana', 27, 1000)
]
# Criando variável temporária
datatemp = vendas
print('Ordenando por pontos:')
# Ordenando valores por pontos
for c in range (0,len(datatemp)):
  for i in range(0,len(datatemp)):
    if datatemp[c][2] > datatemp[i][2]:
      swap = datatemp[i]
      datatemp[i] = datatemp[c]
      datatemp[c] = swap
# Mostra o resultado
print(datatemp)
print('Ordenando por idade, mantendo a ordem de pontos:')
# Ordenando valores por idade, mantendo a ordem de pontuação
for c in range (0,len(datatemp)):
  for i in range(0,len(datatemp)):
    if datatemp[c][2] == datatemp[i][2]:
      if datatemp[c][1] > datatemp[i][1]:
        swap = datatemp[i]
        datatemp[i] = datatemp[c]
        datatemp[c] = swap
# Mostra o resultado
print(datatemp)