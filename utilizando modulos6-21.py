import pygame
#iniciado o mixer
pygame.mixer.init()

#iniciado o pygame
pygame.init()

pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play(loops=0,start=0.0)
pygame.event.wait()
