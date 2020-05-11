#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Mac Gyver escape game
Video game with Mac Gyver trying to ecape from a labyrinth. He must collect tool
to go down the exit guard.

Script Python
Files : macgyver.py, classes.py, level_1, + images
"""

import pygame
from pygame.locals import *

from classes.map import *
from classes.character import *
from classes.settings import *
from classes.display import *

pygame.init()

def main():
    """ Main fonction to launch the game"""

    window = pygame.display.set_mode((NB_SPRITE_WIDTH * SIZE_SPRITE,
                                      NB_SPRITE_HEIGHT * SIZE_SPRITE))
    pygame.display.set_caption(TITRE_FENETRE)
    display = Display(window)

    while display.launchgame:
        # Home loop display with 3 screen depending of the game status

        window.blit(display.homeimage, (0, 0))
        display.game_status_screen(display.status)

        pygame.display.flip()

        while display.homepage:
        # HOME LOOP

            # FPS limitation
            pygame.time.Clock().tick(30)

            # Interact with user to define the next step (exit or play)
            display.event_user_homepage()

        # select level checking before loading
        if display.select_level != 0:

            # Map generation & display
            generate = Map(display.select_level)
            generate.parse_file()
            generate.insert_tool()
            display.map_picture(generate.structure)

            # Mac Gyver first generation
            mac_gyver = Character(generate.structure, "MacGyver")

        while display.game_start:
            # Loop game

            # FPS limitation
            pygame.time.Clock().tick(30)

            for event in pygame.event.get():
                # keyboard event management

                # if quit we stop all
                if event.type == QUIT:
                    display.game_start = 0
                    display.launchgame = 0

                elif event.type == KEYDOWN:
                    # Escape press => comeback to menu
                    if event.key == K_ESCAPE:
                        display.game_start = 0

                    # Move keyboard
                    elif event.key == K_RIGHT:
                        mac_gyver.movement('right')
                    elif event.key == K_LEFT:
                        mac_gyver.movement('left')
                    elif event.key == K_UP:
                        mac_gyver.movement('up')
                    elif event.key == K_DOWN:
                        mac_gyver.movement('down')

            # Display moves
            window.blit(display.background, (0, 0))
            display.map_picture(generate.structure)
            window.blit(mac_gyver.picture, (mac_gyver.pixel_x, mac_gyver.pixel_y))
            pygame.display.flip()

            # Final boss with backpack checking
            if generate.structure[mac_gyver.sprite_y][mac_gyver.sprite_x] == 'e':
                display.game_start = 0
                if mac_gyver.backpack == 3:
                    # rajouter loingueur liste pour code plus propre
                    display.status = "success"
                else:
                    display.status = "fail"


if __name__ == "__main__":
    main()
