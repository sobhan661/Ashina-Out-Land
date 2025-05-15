import sys
import pygame
from Setting import Settings

class Game:
    """Overall class to manage game assets and behavior"""
    def __init__(self):
        """Initializes pygame and create game resources"""
        pygame.init()
        self.setting = Settings()

        self.screen = pygame.display.set_mode((self.setting.width, self.setting.width))
        pygame.display.set_caption("Ashina Out Land")

        self.clock = pygame.time.Clock()

    def RunGame(self):
        """Starts main loop for the game"""
        while True:
            # Watch for mouse and keyboard events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                # Re draw screen during each pass in the loop
                self.screen.fill(self.setting.bg_color)
                # Make most recently drawn screen visible
                pygame.display.flip()
                # Limit game to 60 fps
                self.clock.tick(60) 
                
if __name__ == "__main__":
    # Make a game instance and run the game
    game = Game()
    game.RunGame()