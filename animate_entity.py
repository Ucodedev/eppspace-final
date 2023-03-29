import pygame
from pygame import image

class AnimateEntity(pygame.sprite.Sprite):

    def __init__(self, sprite_name, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f"assets/{sprite_name}.png")
        self.image = pygame.transform.scale(self.image, self.size)
        self.images = animations.get(sprite_name)
        self.current_image = 0
        self.isAnimate = False

    def animate(self, loop=False):
        if self.isAnimate:
            self.current_image += 1
            if self.current_image >= len(self.images):
                self.current_image = 0

                if loop is False:
                    self.isAnimate = False

            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)

    def start_animation(self):
        self.isAnimate = True




# ----------------------------------------------------------------
# Chargement automatique des images pour animer les entitées

def load_animations_images(sprite_name, sprite_number):
    images = []
    path = f"assets/{sprite_name}/{sprite_name}"

    for num in range(1, sprite_number):
        image_path = path + str(num) + ".png"
        images.append(pygame.image.load(image_path))

    return images

animations = {
    "spaceship" : load_animations_images("spaceship", 3),
    "asteroid" : load_animations_images("asteroid", 1),
    "missil" : load_animations_images("missil", 3)
}