nome = str(input('Nome: ')).strip().capitalize()
media = float(input(f'Média de {nome}: '))
situacao = ' '
if media >= 7:
    situacao = 'APROVADO'
else:
    situacao = 'REPROVADO'
aluno = {'Nome': nome, 'Média': media, 'Situação': situacao}
for k,v in aluno.items():
    print(f'{k} é igual a {v}')
