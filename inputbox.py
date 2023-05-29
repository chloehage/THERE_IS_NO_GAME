import pygame as pygame

class InputBox():
    def __init__(self, x, y, w, h, text="ENTRE TON NOM"):
        # création d'un rectangle
        self.rect = pygame.Rect(x, y, w, h)
        # couleur de base
        self.color_inactive = pygame.Color("white")
        # couleur quand on active le bouton
        self.color_active = pygame.Color("white")
        # couleur par défaut
        self.color = self.color_inactive
        self.text = text
        self.font = pygame.font.SysFont("Arial", 18, 0)
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False
        self.fait = False
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos): # si la souris est sur le bouton
                self.active = not self.active
                self.text = ""
            else:
                self.active = False
            if self.active:
                self.color = self.color_active
            else:
                self.color = self.color_inactive
            if event.type == pygame.KEYDOWN:
                if self.active:
                    if event.key == pygame.K_RETURN: # entrer le nom
                        print(self.text)
                        self.fait = True
                    elif event.key == pygame.K_BACKSPACE: # supprimer le dernier caractère
                        self.text = self.text[:-1]
                    else:
                        self.text += event.unicode # ajouter un caractère
                    self.txt_surface = self.font.render(self.text, True, self.color)
                    
    def update(self):
        width = max(180, self.txt_surface.get_width()+10)
        self.rect.w = width
        
    def draw(self, ecran):
        ecran.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(ecran, self.color, self.rect, 2)
                        
