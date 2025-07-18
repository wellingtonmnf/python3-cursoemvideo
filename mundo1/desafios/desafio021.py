import pygame
import os
# Checa o caminho atual no diretório
print('Diretório atual:', os.getcwd())
# Define o caminho do arquivo de áudio
caminho_arquivo = '../../audio/test01.mp3'
# Verifica se o arquivo existe
if os.path.exists(caminho_arquivo):
    print("✅ Arquivo encontrado!")

    pygame.init()
    pygame.mixer.music.load(caminho_arquivo)
    pygame.mixer.music.play()
    # Aguarda a música tocar
    while pygame.mixer.music.get_busy():
        pygame.time.wait(100)

else:
    print("❌ Arquivo NÃO encontrado no caminho:", caminho_arquivo)
    print("Arquivos na pasta atual:", os.listdir('.'))