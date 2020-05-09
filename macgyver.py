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

from classes import *
from settings import *

pygame.init()

def main():
    """ Main fonction to launch the game"""

    window = pygame.display.set_mode((NB_SPRITE_WIDTH * SIZE_SPRITE,
                                      NB_SPRITE_HEIGHT * SIZE_SPRITE))
    titre_fenetre = "Mac Gyver needs you"
    pygame.display.set_caption(titre_fenetre)
    play_game_main = True
    game_status = "try"

    while play_game_main:
        # Home loop display with 3 screen dependinf of the game status

        home = pygame.image.load("images/home.jpg").convert()
        window.blit(home, (0, 0))

        if game_status == "success":
            # display succes menu
            success = pygame.image.load("images/success.png").convert_alpha()
            window.blit(success, (38, 200))

        elif game_status == "fail":
            # display fail menu
            fail = pygame.image.load("images/fail.png").convert_alpha()
            window.blit(fail, (38, 200))
            macgyver = pygame.image.load("images/MacGyver_dead.png").convert_alpha()
            window.blit(macgyver, (87, 134))
            villain = pygame.image.load("images/villain_happy.png").convert_alpha()
            window.blit(villain, (476, 578))

        elif game_status == "try":
            # display home menu
            macgyver = pygame.image.load("images/MacGyver.png").convert_alpha()
            window.blit(macgyver, (87, 134))
            villain = pygame.image.load("images/guard.png").convert_alpha()
            window.blit(villain, (476, 524))

        pygame.display.flip()

        # Var set to true for the loop
        game_start = True
        homepage = True

        while homepage:
        # HOME LOOP

            # FPS limitation
            pygame.time.Clock().tick(30)

            for event in pygame.event.get():

                # In case of exit by user
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    homepage = 0
                    game_start = 0
                    play_game_main = 0
                    game_status = "try"
                    select_level = 0

                elif event.type == KEYDOWN:
                    # Select level 1 to launch the game and
                    # set var homepage to false in order to quit the loop
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
            generate.display(window)

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
                    play_game_main = 0

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
            window.blit(generate.background, (0, 0))
            generate.display(window)
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
