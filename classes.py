#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Class for Mac Gyver video game
2 class :
1 - map
2 - character
"""

import random

import pygame
from pygame.locals import *

from settings import *

class Map:
    """ Map generator """

    def __init__(self, fichier):

        self.fichier = fichier
        self.structure = []
        self.wall = pygame.image.load(IMAGE_WALL).convert()
        self.background = pygame.image.load(IMAGE_BG).convert()
        self.exit = pygame.image.load(IMAGE_EXIT).convert_alpha()
        # random.shuffle(IMAGE_TOOL)
        self.tool = IMAGE_TOOL

    def parse_file(self):
        """ Generating map from a file. It's a list wich contains other lists."""
        with open(self.fichier, "r") as fichier:
            map_structure = []

            for line in fichier:
                line_structure = []

                for sprite in line:
                    if sprite != '\n':
                        line_structure.append(sprite)

                map_structure.append(line_structure)

            # Generate random position for tool and insertion in the map structure
            i = 0
            while i != len(IMAGE_TOOL):
                random_line = random.choice(map_structure)
                random_line_position = map_structure.index(random_line)
                random_sprite = random.randint(0, len(random_line)-1)
                if random_line[random_sprite] == '0':
                    random_line[random_sprite] = 't'
                    map_structure[random_line_position] = random_line
                    i += 1

            self.structure = map_structure

    # @property
    # def tool(self):
    #     return self._tool

    def display(self, fenetre):
        """ Display map on pygame module
        Parse structure map and display the correct sprite"""

        list_tool = self.tool
        nb_tool = 0
        line_position = 0
        for ligne in self.structure:
            # parse line in the structure map
            sprite_position = 0
            for sprite in ligne:
                # parse sprite in each ligne and calculate the x&y pos
                x_axis_sprite = sprite_position * SIZE_SPRITE
                y_axis_sprite = line_position * SIZE_SPRITE

                if sprite == 'w':
                    # w = wall
                    fenetre.blit(self.wall, (x_axis_sprite, y_axis_sprite))

                elif sprite == 'e':
                    # e = exit
                    fenetre.blit(self.exit, (x_axis_sprite, y_axis_sprite))

                elif sprite == 't' and nb_tool < len(list_tool):
                    # t = tool
                    pic_random = list_tool[nb_tool]
                    nb_tool += 1
                    tool = pygame.image.load(pic_random).convert_alpha()
                    fenetre.blit(tool, (x_axis_sprite, y_axis_sprite))
                    # import pdb; pdb.set_trace()
                sprite_position += 1
            line_position += 1

# Testing code for prompt
# map = Map('level_1')
# map.initiate()
# print("Hello")
# print(map.structure)
#  and self.tool != []

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
                    if self.level.structure[self.sprite_y][self.sprite_x+1] == 't':
                        self.level.structure[self.sprite_y][self.sprite_x+1] = '0'
                        self.backpack += 1
                    self.sprite_x += 1
                    self.pixel_x = self.sprite_x * SIZE_SPRITE

        # left move
        if direction == 'left':
            if self.sprite_x > 0:
                if self.level.structure[self.sprite_y][self.sprite_x-1] != 'w':
                    if self.level.structure[self.sprite_y][self.sprite_x-1] == 't':
                        self.level.structure[self.sprite_y][self.sprite_x-1] = '0'
                        self.backpack += 1
                    self.sprite_x -= 1
                    self.pixel_x = self.sprite_x * SIZE_SPRITE

        # move up
        if direction == 'up':
            if self.sprite_y > 0:
                if self.level.structure[self.sprite_y-1][self.sprite_x] != 'w':
                    if self.level.structure[self.sprite_y-1][self.sprite_x] == 't':
                        self.level.structure[self.sprite_y-1][self.sprite_x] = '0'
                        self.backpack += 1
                    self.sprite_y -= 1
                    self.pixel_y = self.sprite_y * SIZE_SPRITE

        # move down
        if direction == 'down':
            if self.sprite_y < (NB_SPRITE_HEIGHT - 1):
                if self.level.structure[self.sprite_y+1][self.sprite_x] != 'w':
                    if self.level.structure[self.sprite_y+1][self.sprite_x] == 't':
                        self.level.structure[self.sprite_y+1][self.sprite_x] = '0'
                        self.backpack += 1
                    self.sprite_y += 1
                    self.pixel_y = self.sprite_y * SIZE_SPRITE
