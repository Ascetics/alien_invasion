import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    """
    管理外星人的类
    """
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        # 外星人图像，初始位置左上角附近
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
