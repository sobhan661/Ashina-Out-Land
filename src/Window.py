import sys
import pygame

class Window:
    """Overall class to manage game assets and behavior"""
    def __init__(self):
        """Initializes pygame and create game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode(1200, 800)
        pygame.display.set_caption("Ashina Out Land")