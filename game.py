import pygame
from entities.spaceship import Spaceship
from entities.asteroid import Asteroid

class Game:

    def __init__(self):
        self.is_playing = False
        self.spaceship = Spaceship(self)
        self.players = pygame.sprite.Group()
        self.players.add(self.spaceship)
        self.monsters = pygame.sprite.Group()
        self.pressed_keys = {}
        self.score = 0
        self.font = pygame.font.Font("assets/fonts/gamer.ttf", 25)

    def start(self):
        self.is_playing = True
        self.spawn_entity(Asteroid)
        self.spawn_entity(Asteroid)
        self.spawn_entity(Asteroid)
        self.spawn_entity(Asteroid)

    def update(self, frame):

        frame.blit(self.spaceship.image, self.spaceship.rect)

        score_text = self.font.render(f"Score : {self.score}", 1, (255, 20, 10))
        frame.blit(score_text, (20, 20))

        self.spaceship.update_animation()
        self.spaceship.projectiles.draw(frame)
        self.spaceship.update_health_bar(frame)

        for projectile in self.spaceship.projectiles:
            projectile.move()

        self.monsters.draw(frame)

        for monster in self.monsters:
            monster.down()
            monster.update_health_bar(frame)

        if self.pressed_keys.get(pygame.K_RIGHT) and (self.spaceship.rect.x + self.spaceship.rect.width) <= frame.get_width():
            self.spaceship.right()
        elif self.pressed_keys.get(pygame.K_LEFT) and self.spaceship.rect.x >= 0:
            self.spaceship.left()
    
    def spawn_entity(self, entity_classname):
        self.monsters.add(entity_classname.__call__(self))

    def check_collide(self, sprite, sprite_group):
        return pygame.sprite.spritecollide(sprite, sprite_group, False, pygame.sprite.collide_mask)

    def game_over(self):
        self.is_playing = False
        self.spaceship.health = self.spaceship.max_health
        self.monsters = pygame.sprite.Group()
        self.spaceship.rect.x = self.spaceship.default_x
        self.score = 0

    def add_score(self, score_amount):
        self.score += score_amount
        