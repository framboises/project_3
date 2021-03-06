#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Mac Gyver escape game
Video game with Mac Gyver trying to ecape from a labyrinth. He must collect
tool
to go down the exit guard.

Script Python
Files : macgyver.py, classes.py, level_1, + images
"""

import pygame

from macgyver.map import Map
from macgyver.character import Character
from macgyver.display import Display
from macgyver.settings import (
    NB_SPRITE_WIDTH,
    SIZE_SPRITE,
    NB_SPRITE_HEIGHT,
    TITRE_FENETRE,
    IMAGE_MACGYVER
)

pygame.init()


def main():
    """ Main fonction to launch the game"""

    window = pygame.display.set_mode(
        (NB_SPRITE_WIDTH * SIZE_SPRITE, NB_SPRITE_HEIGHT * SIZE_SPRITE)
    )
    pygame.display.set_caption(TITRE_FENETRE)
    display = Display(window)

    while display.launchgame:
        # Home loop display with 3 screen depending of the game status

        window.blit(display.homeimage, (0, 0))
        display.game_status_screen(display.status)

        pygame.display.flip()

        while display.homepage:
            # HOME LOOP

            # FPS limitation
            pygame.time.Clock().tick(30)

            # Interact with user to define the next step
            # (exit or play(F1 if 1 level))
            display.event_user_homepage()

        # select level checking before loading
        if display.select_level != 0:

            # Map generation & display
            mapping = Map(display.select_level)
            mapping.parse_file()
            mapping.insert_tool()
            display.map_picture(mapping.structure)

            # Mac Gyver first generation
            mac_gyver = Character(
                mapping.structure,
                "MacGyver",
                pygame.image.load(IMAGE_MACGYVER).convert_alpha()
                )
            display.backpack()

        while display.game_start:
            # Loop game

            # FPS limitation
            pygame.time.Clock().tick(30)

            # Input keyboard for the player MacGyver
            display.event_user_ingame(mac_gyver)

            # Display moves
            window.blit(display.background, (0, 0))
            display.map_picture(mapping.structure)
            window.blit(mac_gyver.picture, (mac_gyver.pixel_x,
                                            mac_gyver.pixel_y))
            display.backpack(mac_gyver.backpack_counter)
            pygame.display.flip()

            # Final boss with backpack checking
            if mapping.structure[mac_gyver.sprite_y][mac_gyver.sprite_x]\
               == "e":
                display.game_start = 0
                if mac_gyver.backpack_counter == 3:
                    # rajouter loingueur liste pour code plus propre
                    display.status = "success"
                else:
                    display.status = "fail"


if __name__ == "__main__":
    main()
