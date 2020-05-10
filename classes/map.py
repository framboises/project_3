#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Class for Mac Gyver video game
Class for generating the map and the movement
"""

import random
# import logging

from classes.settings import *

class Map:
    """ Map generator """

    def __init__(self, fichier):

        self.fichier = fichier
        self.structure = []
        self.tool = list(IMAGE_TOOL)

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

            self.structure = map_structure

    def insert_tool(self):
        """ Generate random position for tool and insertion in the map structure"""

        random.shuffle(self.tool)
        tool_insert = list(self.tool)
        i = 0
        while i != len(self.tool):
            random_line = random.choice(self.structure)
            random_line_position = self.structure.index(random_line)
            random_sprite = random.randint(0, len(random_line)-1)
            if random_line[random_sprite] == '0':
                random_line[random_sprite] = [tool_insert.pop(0),
                                              random_line_position, random_sprite]
                self.structure[random_line_position] = random_line
                # log warning for insert tool duplicate
                # logging.warning(self.structure)
                i += 1

    # Insérer ici la gestion du plateau permettant de vérifier le mouvement de mac gyver
