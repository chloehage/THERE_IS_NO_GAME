import pygame as pygame

class ImputBox(self, x, y, w, h, text="ENTRE TON NOM"):
    self.rect = pygame.Rect(x, y, w, h)
    self.color_inactive = pygame.Color("black")
    self.color_active = pygame.Color("white")
    self.color = self.color_inactive
    self.text = text
    self.font = pygame.font.Sysfont("Arial", 18, 0)
    self.txt_surface = self.font.render(text, True, self.color)
    self.active = False
    self.fait = False
    
def handle_event(self, event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if self.rect.collidepoint(event.pos):
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
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.fait = True
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = self.font.render(self.text, True, self.color)
                
def update(self):
    width = max(180, self.txt_surface.get_width()+10)
    self.rect.w = width
    
def draw(self, screen):
    screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
    pygame.draw.rect(screen, self.color, self.rect, 2)
                    