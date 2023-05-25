import pygame as pygame
from random import randint
import inputbox

pygame.init()

ecran = pygame.display.set_mode((800,800))
pygame.display.set_caption("THERE IS NO GAME")


x,y = 370,370
image = pygame.image.load("du-son.png")
image = pygame.transform.scale(image, (100,100))
image.set_alpha(255)
musique = pygame.mixer.music.load("ascenseur.mp3")
ecran.blit(image, (x,y))

def coupe_music(event,x,y,mouse):
    ecran.blit(image, (x,y))
    if event.type == pygame.MOUSEBUTTONDOWN:
        if x<mouse[0] and mouse[0]<x+100 and y<mouse[1] and mouse[1]<y+100:
            pygame.mixer.music.pause()
            image.set_alpha(0)
    pygame.display.flip()
    

def multiple(event,x,y,mouse):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if x<mouse[0] and mouse[0]<x+100 and y<mouse[1] and mouse[1]<y+100:
            x,y = randint(0,700), randint(0,700)
            print(x,y)
            ecran.blit(image, (x,y))
    pygame.display.flip()
    

running = True
pygame.mixer.music.play()


while running == True:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    multiple(event,x,y,mouse)
        
pygame.quit()
