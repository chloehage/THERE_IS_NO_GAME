import pygame

pygame.init()

ecran = pygame.display.set_mode((800,800))

running = True

image = pygame.image.load("du-son.png")
image = pygame.transform.scale(image, (100,100))
musique = pygame.mixer.music.load("ascenseur.mp3")


pygame.mixer.music.play()



while running == True:
    ecran.blit(image, (370,370))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    
            

    
pygame.quit()