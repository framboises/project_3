#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Class for Mac Gyver video game
Class for display - home menu
"""

import pygame
from pygame.locals import (
    QUIT,
    KEYDOWN,
    K_ESCAPE,
    K_F1,
    K_RIGHT,
    K_LEFT,
    K_UP,
    K_DOWN
)

from .settings import (
    IMAGE_WALL,
    IMAGE_BACKPACK,
    IMAGE_BG,
    IMAGE_EXIT,
    IMAGE_HOME,
    SIZE_SPRITE,
    IMAGE_TOOL,
)


class Display:
    """docstring for ClassName"""

    def __init__(self, window):
        self.wall = pygame.image.load(IMAGE_WALL).convert()
        self.backpack_list = IMAGE_BACKPACK
        self.background = pygame.image.load(IMAGE_BG).convert()
        self.exit = pygame.image.load(IMAGE_EXIT).convert_alpha()
        self.window = window
        self.map = []
        self.status = "try"
        self.launchgame = True
        self.game_start = True
        self.homepage = True
        self.homeimage = pygame.image.load(IMAGE_HOME).convert()
        self.select_level = 0
        self.player = 0

    def map_picture(self, structure):
        """ Display map on pygame module
        Parse structure map and display the correct sprite"""

        self.map = structure
        tool_counter = 0
        line_position = 0
        for ligne in self.map:
            # parse line in the structure map
            sprite_position = 0
            for sprite in ligne:
                # parse sprite in each ligne and calculate the x&y pos
                x_axis_sprite = sprite_position * SIZE_SPRITE
                y_axis_sprite = line_position * SIZE_SPRITE

                if sprite == "w":
                    # w = wall
                    self.window.blit(self.wall, (x_axis_sprite, y_axis_sprite))

                elif sprite == "e":
                    # e = exit
                    self.window.blit(self.exit, (x_axis_sprite, y_axis_sprite))

                elif isinstance(sprite, list)\
                        and tool_counter < len(IMAGE_TOOL):
                    # t = tool
                    tool_counter += 1
                    tool = pygame.image.load(sprite[0]).convert_alpha()
                    self.window.blit(tool, (x_axis_sprite, y_axis_sprite))
                    # import pdb; pdb.set_trace()
                sprite_position += 1
            line_position += 1

    def backpack(self, backpack_counter=0):
        """ test """

        item = self.backpack_list[backpack_counter]
        backpack_pic = pygame.image.load(item).convert_alpha()
        self.window.blit(backpack_pic, (200, 0))

    def game_status_screen(self, status):
        """ Display the correct screen based on the game status
        success if the player win, fail if he loose or try at
        the beginning or if he restart """

        self.game_start = True
        self.homepage = True
        self.status = status
        if self.status == "success":
            # display succes menu
            success = pygame.image.load("images/success.png").convert_alpha()
            self.window.blit(success, (38, 200))

        elif self.status == "fail":
            # display fail menu
            fail = pygame.image.load("images/fail.png").convert_alpha()
            self.window.blit(fail, (38, 200))
            macgyver = pygame.image.load(
                "images/MacGyver_dead.png"
                ).convert_alpha()
            self.window.blit(macgyver, (87, 134))
            villain = pygame.image.load(
                "images/villain_happy.png"
                ).convert_alpha()
            self.window.blit(villain, (476, 578))

        elif self.status == "try":
            # display home menu
            macgyver = pygame.image.load("images/MacGyver.png").convert_alpha()
            self.window.blit(macgyver, (87, 134))
            villain = pygame.image.load("images/guard.png").convert_alpha()
            self.window.blit(villain, (476, 524))

    def event_user_homepage(self):
        """ Loop for key action by user, quit the game, restart and select the
        level. For now we have only one level, but the system is ready for
        futur map. """

        for event in pygame.event.get():

            # In case of exit by user
            if event.type == QUIT or event.type == KEYDOWN \
                    and event.key == K_ESCAPE:
                self.homepage = 0
                self.game_start = 0
                self.launchgame = 0
                self.status = "try"
                self.select_level = 0

            elif event.type == KEYDOWN:
                # Select level 1 to launch the game and
                # set var homepage to false in order to quit the loop
                # We can implement more level easily
                if event.key == K_F1:
                    self.homepage = 0
                    self.status = "try"
                    self.select_level = "level/level_1"

    def event_user_ingame(self, player):
        """ Input user on keyboard for movement or leaving game """

        self.player = player
        for event in pygame.event.get():
            # keyboard event management

            # if quit we stop all
            if event.type == QUIT:
                self.game_start = 0
                self.launchgame = 0

            elif event.type == KEYDOWN:
                # Escape press => comeback to menu
                if event.key == K_ESCAPE:
                    self.game_start = 0

                # Move keyboard
                elif event.key == K_RIGHT:
                    self.player.move("right")
                elif event.key == K_LEFT:
                    self.player.move("left")
                elif event.key == K_UP:
                    self.player.move("up")
                elif event.key == K_DOWN:
                    self.player.move("down")
