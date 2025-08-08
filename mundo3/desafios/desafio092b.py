from datetime import datetime
atual = datetime.today().year
pessoa = dict()
pessoa['nome'] = str(input('Nome: ')).strip().capitalize()
nasc = int(input('Ano de Nascimento: '))
pessoa['idade'] = atual - nasc
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input('Ano de Contratação: '))
    pessoa['salario'] = float(input('Salário: R$ '))
    pessoa['aposentadoria'] = (35 - (atual - pessoa['contratacao'])) + pessoa['idade']
print('-=' * 30)
for k, v in pessoa.items():
    print(f'  - {k} tem o valor {v}')
