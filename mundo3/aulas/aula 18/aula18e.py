galera = list() # Cria uma lista vazia
dado = list() # Cria uma lista vazia para receber DADOS TEMPORÁRIOS
for c in range(0,3):
    dado.append(str(input('Nome: '))) # Adiciona nome na lista dado
    dado.append(int(input('Idade: '))) # Adiciona idade na lista dado
    galera.append(dado[:]) # Cria uma cópia da lista dado e adiciona como item na lista galera
    dado.clear() # limpa os dados da lista dado

print(galera) # Imprime galera
