import pygame
pygame.init()
# The song archive needs to be on the same directory
pygame.mixer.music.load('song.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy(): pass
