from datetime import date

ano = int(input('Digite o ano a ser analisado (0 para o ano atual): '))

if ano == 0:
    ano = date.today().year # Pega o valor do ano atual configurado no relógio da máquina do usuário

if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} NÃO é bissexto')