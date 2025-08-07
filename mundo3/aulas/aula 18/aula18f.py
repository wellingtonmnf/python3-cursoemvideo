galera = list() # Cria uma lista vazia
dado = list() # Cria uma lista vazia para receber DADOS TEMPORÁRIOS
for c in range(0,3):
    dado.append(str(input('Nome: '))) # Adiciona nome na lista dado
    dado.append(int(input('Idade: '))) # Adiciona idade na lista dado
    galera.append(dado) # Adiciona a lista dado como item na lista galera
    dado.clear() # limpa os dados da lista dado

    # Isso causará um erro, pois a cada inserção, a lista dado será limpa.
    # Após isso, será reinserida e constará com novos valores em todas as suas
    # instâncias dentro da lista galera, que logo em seguida serão
    # apagadas novamente.
    # Ao final do ciclo, galera será uma lista com listas vazias

print(galera) # Imprime galera
