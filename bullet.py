import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    """
    管理飞船发射的子弹
    """
    def __init__(self, ai_game):
        super.__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # 为什么要先在0,0位置画出子弹，再移动到飞船头部呢
        # 为了方便计算位置
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_width)
        self.rect.midtop = self.screen.rect.midtop

        # 小数存储子弹的位置
        self.y = float(self.rect.y)

    def update(self):
        """
        子弹向上飞
        """
        # 更新子弹位置的小数值
        self.y -= self.settings.bullet_speed
        # 更新子弹位置
        self.rect.y = self.y

    def draw_bullet(self):
        """
        画出子弹
        """
        pygame.draw(self.screen, self.color, self.rect)
        