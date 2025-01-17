import pygame

# Import settings with colors
from settings import Colors

# Create class
class Menu:

    # Initialize class
    def __init__(self, screen):
        self.screen = screen
        self.options = ["Play!", "Quit"]
        self.selected_option = 0
        self.font = pygame.font.Font(None, 46)
        self.selected_option_font = pygame.font.Font(None, 73)

    # Drawing method
    def draw(self):
        for i in range(len(self.options)):
            if i == self.selected_option:
                text = self.selected_option_font.render(self.options[i], True, Colors.green)
            else:
                text = self.font.render(self.options[i], True, Colors.white)
            text_rect = text.get_rect(topleft = (90, 70 + 50 * i))
            self.screen.blit(text, text_rect)
    
    # Handling keys
    def handle_keys(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_UP, pygame.K_w]:
                self.selected_option -= 1
            elif event.key in [pygame.K_DOWN, pygame.K_s]:
                self.selected_option += 1
            if self.selected_option > 1:
                self.selected_option -= 1
            if self.selected_option <= -1:
                self.selected_option += 1