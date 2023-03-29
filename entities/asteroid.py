import pygame, random

from animate_entity import AnimateEntity


class Asteroid(AnimateEntity):

    def __init__(self, game):
        super().__init__("asteroid", (39, 38))
        self.game = game
        self.max_health = random.randint(5, 7)
        self.health = self.max_health
        self.damage = 5
        self.velocity = random.randint(3, 5)
        self.image = pygame.image.load("assets/asteroid.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0 + random.randint(0, 450)
        self.rect.y = 0
        self.loot_score = 10
        self.diagonal = random.randint(-3, 3)
        self.start_animation()

    def update_animation(self):
        self.animate(loop=True)

    def down(self):

        if not self.game.check_collide(self, self.game.players):
            self.rect.y += self.velocity
        else:
            self.game.spaceship.add_damage(self.damage)

        # check if the asteroid is out of the screen
        if self.rect.y > 550:
            self.rect.y = 0
            self.rect.x = random.randint(0, 450)

    def update_health_bar(self, frame):
        health_color = (111, 210, 46)  # RGB = Red Green Blue
        health_background_color = (111, 20, 20)

        health_background_position = [self.rect.x + ((self.image.get_width() / 2) - (self.max_health / 2)),
                                      self.rect.y - 20, self.max_health, 5]

        rect_bg_position = pygame.draw.rect(frame, health_background_color, health_background_position)

        health_position = [rect_bg_position.x, self.rect.y - 20, self.health, 5]
        pygame.draw.rect(frame, health_color, health_position)

    def add_damage(self, amount_damage):
        self.health -= amount_damage

        if self.health <= 0:
            self.rect.x = 1280 + random.randint(0, 10)
            self.health = self.max_health
            self.velocity = random.randint(1, 3)
            self.game.add_score(self.loot_score)
