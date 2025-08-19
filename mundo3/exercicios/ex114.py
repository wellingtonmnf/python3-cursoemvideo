import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento')
else:
    print('Consegui acessar o site Pudim com sucesso!')
    print(site.read()) # Esse comando consegue acessar_todo o conteúdo HTML da página
