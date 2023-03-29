import pygame

class Missile(pygame.sprite.Sprite):

    def __init__(self, entity):
        super().__init__()
        self.image = pygame.image.load("assets/missil.png")
        self.default_image = self.image
        self.entity = entity
        self.rect = self.image.get_rect()
        self.rect.x = self.entity.rect.x + 28
        self.rect.y = self.entity.rect.y + self.image.get_width()
        self.velocity = 5
        self.angle = 0

    def move(self):

        self.rect.y -= self.velocity

        for monster in self.entity.game.check_collide(self, self.entity.game.monsters):
            self.remove()
            monster.add_damage(self.entity.damage)

        if self.rect.y < 0:
            self.remove()

    def remove(self):
        self.entity.projectiles.remove(self)
