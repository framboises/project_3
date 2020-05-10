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
from classes.main_game import *
from classes.home_game import *

pygame.init()

def main():
    """ Main fonction to launch the game"""

    window = pygame.display.set_mode((NB_SPRITE_WIDTH * SIZE_SPRITE,
                                      NB_SPRITE_HEIGHT * SIZE_SPRITE))
    pygame.display.set_caption(TITRE_FENETRE)
    launch_game = True
    game_status = "try"

    while launch_game:
        # Home loop display with 3 screen depending of the game status

        # Var set to true for the loop
        game_start = True
        homepage = True
        home = pygame.image.load("images/home.jpg").convert()
        window.blit(home, (0, 0))
        display = Display(window)
        display.game_status_screen(game_status)

        pygame.display.flip()

        while homepage:
        # HOME LOOP

            # FPS limitation
            pygame.time.Clock().tick(30)

            for event in pygame.event.get():

                # In case of exit by user
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    homepage = 0
                    game_start = 0
                    launch_game = 0
                    game_status = "try"
                    select_level = 0

                elif event.type == KEYDOWN:
                    # Select level 1 to launch the game and
                    # set var homepage to false in order to quit the loop
                    # We can implement more level easily
                    if event.key == K_F1:
                        homepage = 0
                        select_level = "level_1"
                        game_status = "try"

        # select level checking before loading
        if select_level != 0:

            # Map first generation
            generate = Map(select_level)
            generate.parse_file()
            generate.insert_tool()
            display.map_picture(generate.structure)

            # Mac Gyver first generation
            mac_gyver = Character("images/MacGyver.png", generate)

        while game_start:
            # Loop game

            # FPS limitation
            pygame.time.Clock().tick(30)

            for event in pygame.event.get():
                # keyboard event management

                # if quit we stop all
                if event.type == QUIT:
                    game_start = 0
                    launch_game = 0

                elif event.type == KEYDOWN:
                    # Escape press => comeback to menu
                    if event.key == K_ESCAPE:
                        game_start = 0

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
                game_start = 0
                if mac_gyver.backpack == 3:
                    # rajouter loingueur liste pour code plus propre
                    game_status = "success"
                else:
                    game_status = "fail"


if __name__ == "__main__":
    main()
