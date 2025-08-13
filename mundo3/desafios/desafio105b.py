def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param n: Uma ou mais notas dos alunos (aceita várias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação
    :return: Dicionário com várias informações sobre a situação da turma
    """
    aluno = dict()
    aluno['total'] = len(n)
    aluno['maior'] = max(n)
    aluno['menor'] = min(n)
    aluno['media'] = sum(n)/len(n)

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
