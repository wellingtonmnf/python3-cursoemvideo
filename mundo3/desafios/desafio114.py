import urllib.request

site = 'https://www.pudim.com.br/'
try:
    urllib.request.urlopen(site)
except:
    print('\033[31mO site Pudim não está acessível no momento\033[m')
else:
    print('\033[32mConsegui acessar o site Pudim com sucesso!\033[m')
