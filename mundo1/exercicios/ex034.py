salario = float(input('Digite o salário do funcionário(a): '))
# Solução com condicional simplificada
print(f'Novo salário: R$ {(salario + (salario*10/100)):.2f} | Aumento: 10%' if salario > 1250 else f'Novo salário: R$ {(salario + (salario*15/100)):.2f} | Aumento: 15%')
