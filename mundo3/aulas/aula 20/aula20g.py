def dobra(lst): # O parametro em Python é passado NÃO POR VALOR, mas sim por REFERÊNCIA
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2 # As alterações feitas em 'lst' REFLETIRÃO em 'valores'
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores) # A lista 'valores' é passada por REFERÊNCIA para 'lst'
print(valores) # O resultado é que as alterações feitas no metodo se refletem na variável fora dele
