import sys
import pygame

class Game:
    """Overall class to manage game assets and behavior"""
    def __init__(self):
        """Initializes pygame and create game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Ashina Out Land")

    def RunGame(self):
        """Starts main loop for the game"""
        while True:
            # Watch for mouse and keyboard events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                # Make most recently drawn screen visible
                pygame.display.flip()
                
if __name__ == "__main__":
    # Make a game instance and run the game
    game = Game()
    game.RunGame()