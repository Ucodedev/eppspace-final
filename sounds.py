import pygame


class SoundManager:

    def __init__(self):
        self.sounds = {
            "blaster": pygame.mixer.Sound("sounds/blaster_final.wav"),
            "game_over": pygame.mixer.Sound("sounds/game over.wav"),
            "mainmusic": pygame.mixer.Sound("sounds/mainmusic.wav")
        }

    def play(self, name, loop=0, volume=1.0):
        self.sounds[name].play(loop).set_volume(volume)
