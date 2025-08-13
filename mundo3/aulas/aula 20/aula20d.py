def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


# Programa principal
soma(a=4, b=5) # É possível explicitar os valores dos parâmetros
soma(b=4, a=5) # É possível inverter a ordem dos parâmetros da declaração dos argumentos
# soma(a=4, 5) # NÃO É possível deixar um dos parâmetros sem ser explicitado se outro for
soma(a=7, b=2) # Caso não sejam explicitados os valores dos parâmetros, estes são assumidos automaticamente na ordem de declaração
# soma(3,9,5) # Não é possível passar mais parâmetros que o definido na assunatura da função
