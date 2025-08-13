def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param n: Uma ou mais notas dos alunos (aceita várias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação
    :return: Dicionário com várias informações sobre a situação da turma
    """
    aluno = dict()
    total = maior = menor = soma = 0
    for pos, n in enumerate(n):
        total += 1
        soma += n
        if pos == 0:
            maior = n
            menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n

    aluno['total'] = total
    aluno['maior'] = maior
    aluno['menor'] = menor
    aluno['media'] = soma/total

    if sit == True:
        if aluno['media'] >= 7:
            aluno['situacao'] = 'BOA'
        elif 5 <= aluno['media'] < 7:
            aluno['situacao'] = 'RAZOÁVEL'
        else:
            aluno['situacao'] = 'RUIM'

    return aluno

resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)
