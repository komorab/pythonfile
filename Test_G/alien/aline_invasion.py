#to creat the game about shoot aline
import pygame
import sys
from setting import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien

def run_game():
    'beginning(initialize) and creat a screen object'
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)

    alien = Alien(ai_settings, screen)

    bullets = Group()

#start the main loop of game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_bullets(bullets)
        gf.upadte_screen(ai_settings, screen, ship,alien, bullets)


if __name__=='__main__':
    run_game()