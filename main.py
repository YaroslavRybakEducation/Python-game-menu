import pygame # pip install pygame
import sys
from settings import Colors
from menu import Menu
from ingame import InGame

# Initialize modules
pygame.init()

# Set up the scenes
in_menu = True
in_game = False

# Set up screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = int(SCREEN_WIDTH)

# Creating window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Python Game menu Example")

game_menu = Menu(screen)
ingame = InGame() # Class in game

# Set up clock
clock = pygame.time.Clock()

def main():
    global in_menu, in_game
    while True:
        if in_menu:
            for event in pygame.event.get():
                # Quit the game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                game_menu.handle_keys(event)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if game_menu.options[game_menu.selected_option] == "Quit":
                            pygame.quit()
                            sys.exit()
                        if game_menu.options[game_menu.selected_option] == "Play!":
                            in_menu = False
                            in_game = True
            
            # Drawing
            screen.fill(Colors.blue)
            game_menu.draw()
            pygame.display.update()
            clock.tick(60)
        
        # Inside game
        if in_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        # Returns to menu scene
                        in_game = False
                        in_menu = True
            
            # Drawing
            screen.fill(Colors.blue)
            ingame.draw("Hello world!", 40, 40, Colors.white, screen)
            ingame.draw("Press esc", 40, 60, Colors.white, screen)
            pygame.display.update()
            clock.tick(60)

if __name__ == "__main__":
    main() # Run the game
