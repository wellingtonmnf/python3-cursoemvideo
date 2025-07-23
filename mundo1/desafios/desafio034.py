sal = float(input('Digite o salário do funcionário(a): '))

if sal > 1250.00:
    print(f'Novo salário: R$ {(sal + (sal*10/100)):.2f} | Aumento: \033[7:32m10%\033[m')
else:
    print(f'Novo salário: R$ {(sal + (sal*15/100)):.2f} | Aumento: \033[7:34m15%\033[m')