import pygame

class ShipGame:
    """A class to manage the ship"""
    def __init__(self, ai_game):
        """Initialize the ship and it's starting position"""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Loads ship image and it's rect
        self.image = pygame.image.load("src/images/ship.bmp")
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw ship at it's current location"""

        self.screen.blit(self.image, self.rect)