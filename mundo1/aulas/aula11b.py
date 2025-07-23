a = 3
b = 5
print(f'Os valores são \033[32;40m{a}\033[m e \033[31;40m{b}\033[m')

nome = 'Guanabara'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}

print('Olá, muito prazer me te conhecer, {}{}{}!'.format('\033[4;34m',nome,'\033[m'))
print('Olá, muito prazer me te conhecer, {}{}{}!'.format(cores['amarelo'],nome,cores['limpa']))
print('Olá, muito prazer me te conhecer, {}{}{}!'.format(cores['pretoebranco'],nome,cores['limpa']))