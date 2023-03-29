import pygame
from animate_entity import AnimateEntity

from items.missile import Missile

class Spaceship(AnimateEntity):

    def __init__(self, game):
        super().__init__("spaceship", (64, 64))
        self.game = game
        self.health = 3
        self.max_health = 3
        self.damage = 1
        self.velocity = 3
        self.image = pygame.image.load("assets/spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.x = 215
        self.rect.y = 700
        self.default_x = 275

        self.projectiles = pygame.sprite.Group()

    def right(self):

        if not self.game.check_collide(self, self.game.monsters):
            self.rect.x += self.velocity
        self.start_animation()

    def left(self):
        self.rect.x -= self.velocity
        self.start_animation()

    def shot(self):
        self.projectiles.add(Missile(self))

       # self.game.sound_manager.play('dark_orbe', 0, 0.15) # Son de la boule de magie lancée par le jouer

    def update_animation(self):
        self.animate()

    def update_health_bar(self, frame):
        health_color = (111, 210, 46) # RGB = Red Green Blue
        health_background_color = (111, 20, 20)

        health_background_position = [self.rect.x + ((self.image.get_width() / 2) - (self.max_health / 2)), self.rect.y - 20, self.max_health, 5]

        rect_bg_position = pygame.draw.rect(frame, health_background_color, health_background_position)

        health_position = [rect_bg_position.x, self.rect.y - 20, self.health, 5]
        pygame.draw.rect(frame, health_color, health_position)

    def add_damage(self, amount_damage):
        self.health -= amount_damage

        if self.health <= 0:
            self.game.game_over()
