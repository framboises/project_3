#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Class for Mac Gyver video game
Class for character in the video game
"""
import pygame
from pygame.locals import *

from classes.settings import *

class Character:
    """Generating a character"""

    def __init__(self, picture, level):

        # profile picture
        self.picture = pygame.image.load(picture).convert_alpha()

        # sprite and pixel position of the character
        self.sprite_x = 0
        self.sprite_y = 0
        self.pixel_x = 0
        self.pixel_y = 0
        self.backpack = 0

        # generating map instance
        self.level = level


    def movement(self, direction):
        """ Move character method """

        # right move
        if direction == 'right':
            # border check
            if self.sprite_x < (NB_SPRITE_WIDTH - 1):
                if self.level.structure[self.sprite_y][self.sprite_x+1] != 'w':
                    if isinstance(self.level.structure[self.sprite_y][self.sprite_x+1], list):
                        self.level.structure[self.sprite_y][self.sprite_x+1] = '0'
                        self.backpack += 1
                    self.sprite_x += 1
                    self.pixel_x = self.sprite_x * SIZE_SPRITE

        # left move
        if direction == 'left':
            if self.sprite_x > 0:
                if self.level.structure[self.sprite_y][self.sprite_x-1] != 'w':
                    if isinstance(self.level.structure[self.sprite_y][self.sprite_x-1], list):
                        self.level.structure[self.sprite_y][self.sprite_x-1] = '0'
                        self.backpack += 1
                    self.sprite_x -= 1
                    self.pixel_x = self.sprite_x * SIZE_SPRITE

        # move up
        if direction == 'up':
            if self.sprite_y > 0:
                if self.level.structure[self.sprite_y-1][self.sprite_x] != 'w':
                    if isinstance(self.level.structure[self.sprite_y-1][self.sprite_x], list):
                        self.level.structure[self.sprite_y-1][self.sprite_x] = '0'
                        self.backpack += 1
                    self.sprite_y -= 1
                    self.pixel_y = self.sprite_y * SIZE_SPRITE

        # move down
        if direction == 'down':
            if self.sprite_y < (NB_SPRITE_HEIGHT - 1):
                if self.level.structure[self.sprite_y+1][self.sprite_x] != 'w':
                    if isinstance(self.level.structure[self.sprite_y+1][self.sprite_x], list):
                        self.level.structure[self.sprite_y+1][self.sprite_x] = '0'
                        self.backpack += 1
                    self.sprite_y += 1
                    self.pixel_y = self.sprite_y * SIZE_SPRITE
