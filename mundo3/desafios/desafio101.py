from datetime import datetime


def voto(nasc):
    global idade
    idade = datetime.now().year - nasc
    if idade < 16:
        return 'VOTO NEGADO'
    elif 18 <= idade < 65:
        return 'VOTO OBRIGATÓRIO'
    else:
        return 'VOTO OPCIONAL'

print('-'*25)
idade = 0
ano_nasc = int(input('Ano de nascimento: '))
resp = voto(ano_nasc)
print(f'Com {idade} anos: {resp}.')
