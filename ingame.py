import pygame

class InGame:

    # Initialize class
    def __init__(self):
        self.font = pygame.font.Font(None, 30)
    
    # Drawing method
    # And rendering any texts
    def draw(self, text, x, y, color, screen):
        txt_surface = self.font.render(text, True, color)
        screen.blit(txt_surface, (x, y))