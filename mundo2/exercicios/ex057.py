sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0] #Pega apenas a primeira letra da string

while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: [M/F] ')).upper().strip()
print(f'Sexo {sexo} registrado com sucesso')
