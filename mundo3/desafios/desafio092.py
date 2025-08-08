from datetime import datetime

ano_atual = datetime.today().year

nome = str(input('Nome: ')).strip().capitalize()
ano_nasc = int(input('Ano de nascimento: '))
idade = ano_atual - ano_nasc
ctps = int(input('Carteira de trabalho (0 se não possui): '))

pessoa = {'nome': nome, 'idade': idade, 'ctps': ctps}

if ctps != 0:
    contratacao = int(input('Ano de contratação: '))
    pessoa['contratacao'] = contratacao
    salario = float(input('Salário: R$ '))
    pessoa['salario'] = salario
    # cálculo da aposentadoria
    tempo_trabalhado = ano_atual - contratacao
    tempo_restante = 35 - tempo_trabalhado
    aposentadoria = idade + tempo_restante
    pessoa['aposentadoria'] = aposentadoria

print(pessoa)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')
