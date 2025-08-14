from utilidadesCeV import moeda, dado
# Tem que aceitar valor digitado com vírgula (ex: 850,99)
p = dado.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(p, 80, 35)