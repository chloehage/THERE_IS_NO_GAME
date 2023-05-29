import pygame as pygame
from random import randint
import inputbox

def coupe_music():
    pygame.mixer.music.pause()
    

def multiple(x,y,image):
    for i in range(10):
        x,y = randint(0,700), randint(0,700)
        print(x,y)
        ecran.blit(image, (x,y))
        pygame.display.flip()
        
def nom(inputbox,event):
    inputbox.handle_event(event)
    

pygame.init()

ecran = pygame.display.set_mode((800,800))
pygame.display.set_caption("THERE IS NO GAME")


x,y = 370,370
image = pygame.image.load("du-son.png")
image = pygame.transform.scale(image, (100,100))
image.set_alpha(255)
musique = pygame.mixer.music.load("ascenseur.mp3")
ecran.blit(image, (x,y))

running = True
pygame.mixer.music.play()
state = 0
inputbox = inputbox.InputBox(x,y,400,36)

while running == True:
    mouse = pygame.mouse.get_pos()
    ecran.blit(image, (x,y))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if x<mouse[0] and mouse[0]<x+100 and y<mouse[1] and mouse[1]<y+100:
                if state == 0:
                    coupe_music()
                    state += 1
                elif state == 1:
                    nom(inputbox,event)
                    state += 1
                elif state == 2:
                    multiple(x,y,image)
                    pygame.mixer.music.play()
                    
        
pygame.quit()
