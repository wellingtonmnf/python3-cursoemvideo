import pygame

pygame.init()
pygame.mixer.music.load('../../audio/test01.mp3')
pygame.mixer.music.play()
# este 'while' faz com que o pygame aguarde até a música terminar
while pygame.mixer.music.get_busy():
    pygame.time.wait(100)

# Foi necessária adicionar essa linha para que o arquivo de áudio fosse executado