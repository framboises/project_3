#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Class for Mac Gyver video game
Class for display - home menu
"""

import pygame
from pygame.locals import *

from classes.map import *
from classes.character import *
from classes.settings import *

class Display:
    """docstring for ClassName"""

    def __init__(self, window):
        self.wall = pygame.image.load(IMAGE_WALL).convert()
        self.background = pygame.image.load(IMAGE_BG).convert()
        self.exit = pygame.image.load(IMAGE_EXIT).convert_alpha()
        self.window = window
        self.map = []
        self.status = "try"

    def map_picture(self, structure):
        """ Display map on pygame module
        Parse structure map and display the correct sprite"""

        self.map = structure
        nb_tool_counter = 0
        line_position = 0
        for ligne in self.map:
            # parse line in the structure map
            sprite_position = 0
            for sprite in ligne:
                # parse sprite in each ligne and calculate the x&y pos
                x_axis_sprite = sprite_position * SIZE_SPRITE
                y_axis_sprite = line_position * SIZE_SPRITE

                if sprite == 'w':
                    # w = wall
                    self.window.blit(self.wall, (x_axis_sprite, y_axis_sprite))

                elif sprite == 'e':
                    # e = exit
                    self.window.blit(self.exit, (x_axis_sprite, y_axis_sprite))

                elif isinstance(sprite, list) and nb_tool_counter < len(IMAGE_TOOL):
                    # t = tool
                    nb_tool_counter += 1
                    tool = pygame.image.load(sprite[0]).convert_alpha()
                    self.window.blit(tool, (x_axis_sprite, y_axis_sprite))
                    # import pdb; pdb.set_trace()
                sprite_position += 1
            line_position += 1

    def game_status_screen(self, status):
        """ Display the correct screen based on the game status
        success if the player win, fail if he loose or try at
        the beginning or if he restart """

        self.status = status
        if self.status == "success":
            # display succes menu
            success = pygame.image.load("images/success.png").convert_alpha()
            self.window.blit(success, (38, 200))

        elif self.status == "fail":
            # display fail menu
            fail = pygame.image.load("images/fail.png").convert_alpha()
            self.window.blit(fail, (38, 200))
            macgyver = pygame.image.load("images/MacGyver_dead.png").convert_alpha()
            self.window.blit(macgyver, (87, 134))
            villain = pygame.image.load("images/villain_happy.png").convert_alpha()
            self.window.blit(villain, (476, 578))

        elif self.status == "try":
            # display home menu
            macgyver = pygame.image.load("images/MacGyver.png").convert_alpha()
            self.window.blit(macgyver, (87, 134))
            villain = pygame.image.load("images/guard.png").convert_alpha()
            self.window.blit(villain, (476, 524))

