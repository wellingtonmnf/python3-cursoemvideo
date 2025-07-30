sexo = str(input('Informe o sexo [F/M]: ')).upper().strip()

if sexo != 'M' and sexo != 'F':
    while sexo != 'F' and sexo != 'M':
        print('VALOR INVÁLIDO! Digite "F" para feminino ou "M" para masculino')
        sexo = str(input('Informe o sexo [F/M]: ')).upper().strip()

print('Cadastro validado')
