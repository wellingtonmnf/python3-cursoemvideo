galera = list() # Cria uma lista vazia
dado = list() # Cria uma lista vazia para receber DADOS TEMPORÁRIOS
totmai = totmen = 0
for c in range(0,3):
    dado.append(str(input('Nome: '))) # Adiciona nome na lista dado
    dado.append(int(input('Idade: '))) # Adiciona idade na lista dado
    galera.append(dado[:]) # Cria uma cópia da lista dado e adiciona como item na lista galera
    dado.clear() # limpa os dados da lista dado

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade.')
