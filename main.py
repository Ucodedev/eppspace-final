import pygame
import sys
from game import Game
from sounds import SoundManager

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('sounds/startscreen.wav')
pygame.mixer.music.play()

#variable du jeu
pygame.display.set_caption("Epspace - Bootcamp 2022 EPSI Arras")
frame = pygame.display.set_mode((500, 800))
frame_rect = frame.get_rect()
running = True
clock = pygame.time.Clock()
fps = 60

game = Game()
running = True

# Background home
home_bg = pygame.image.load("assets/background/background_home.png")
home_bg_sized = pygame.transform.scale(
    home_bg, (frame_rect.right, frame_rect.bottom))

# Background level
level_bg = pygame.image.load("assets/background/background_play.png")
level_bg_sized = pygame.transform.scale(level_bg, (frame_rect.right, frame_rect.bottom))
frame.blit(level_bg_sized, (0,0))
pygame.display.flip()

# Logo
logo = pygame.image.load("assets/epspace.png")
logo_rect = logo.get_rect()
logo_rect.x = (frame.get_width() / 2) - (logo.get_width() / 2)
logo_rect.y = 300

# Button
play = pygame.image.load("assets/play.png")
play_sized = pygame.transform.scale(play, (200,100))
play_rect = play_sized.get_rect()
play_rect.x = (frame.get_width() / 2) - (play_sized.get_width() / 2)
play_rect.y = logo.get_height() + 300

#boucle principale
while running:

    if game.is_playing:
        frame.blit(level_bg_sized, (0, 0))
        game.update(frame)  # Je met à jour l'écran de jeu


    else:
        frame.blit(home_bg_sized, (0, 0))
        frame.blit(logo, (logo_rect.x, logo_rect.y))
        frame.blit(play_sized, (play_rect.x, play_rect.y))

    pygame.display.flip()  # Met à jour le contenu de la fenêtre

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if play_rect.collidepoint(event.pos) and not game.is_playing:
                game.start()  # Lancement de la partie

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                game.spaceship.shot()
                pygame.mixer.music.load('sounds/blaster_final.wav')
                pygame.mixer.music.play()


            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
                sys.exit()

            game.pressed_keys[event.key] = True

        elif event.type == pygame.KEYUP:
            game.pressed_keys[event.key] = False
    clock.tick(fps)
