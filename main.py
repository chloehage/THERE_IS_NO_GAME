import pygame as pygame
from random import randint
import inputbox

def coupe_music():
    """
Fonction pour couper la musique quand on clique sur le bouton de volume
"""
    pygame.mixer.music.pause()
    

def multiple(x,y,image):
    """
Fonction pour afficher un nouveau bouton de volume quand on clique sur le premier bouton
"""
    for i in range(10):
        x,y = randint(0,700), randint(0,700)
        print(x,y)
        ecran.blit(image, (x,y))
        pygame.display.flip()
        
def nom(inputbox,ecran):
    """
Fonction pour entrer le nom de l'utilisateur
"""
    for event in pygame.event.get():
        inputbox.handle_event(event)
    inputbox.update()
    inputbox.draw(ecran)
    pygame.display.flip()
    
# lancement des modules inclus dans pygame
pygame.init()
# création d'une fenêtre de 800 par 800
ecran = pygame.display.set_mode((800,800))
pygame.display.set_caption("THERE IS NO GAME")


x,y = 370,370

image = pygame.image.load("du-son.png")
image = pygame.transform.scale(image, (100,100))
image.set_alpha(255)
musique = pygame.mixer.music.load("ascenseur.mp3")

running = True
pygame.mixer.music.play()
# variable pour enchaîner les différentes fonctions
state = 0
# chargement du bouton pour entrer le nom d'utilisateur
inputbox = inputbox.InputBox(310,370,140,32)
ecran.blit(image, (x,y))

# boucle infinie pour laisser la fenêtre ouverte
while running == True:
    mouse = pygame.mouse.get_pos()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # si on clique sur le bouton volume
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if x<mouse[0] and mouse[0]<x+100 and y<mouse[1] and mouse[1]<y+100:
                if state == 0:
                    coupe_music()
                    state += 1
                elif state == 1:
                    pygame.Surface.fill(ecran, [0,0,0])
                    nom(inputbox,ecran)
                    state += 1
                elif state == 2:
                    pygame.Surface.fill(ecran, [0,0,0])
                    ecran.blit(image, (x,y))
                    state += 1
                elif state == 3:
                    multiple(x,y,image)
                    pygame.mixer.music.play()
                    
              
        
pygame.quit()