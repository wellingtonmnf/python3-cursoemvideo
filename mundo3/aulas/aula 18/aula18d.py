galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(p)  # Imprime cada lista com as pessoas
print('-' * 30)
for p in galera:
    print(p[0])  # Imprime apenas o nome das pessoas
print('-' * 30)
for p in galera:
    print(p[1])  # Imprime apenas a idade das pessoas
print('-' * 30)
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')  # Imprime os dados das pessoas de maneira formatada
