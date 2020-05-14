#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Class for Mac Gyver video game
Class for generating the map and the movement
"""

import random

from .settings import IMAGE_TOOL


class Map:
    """ Map generator """

    def __init__(self, fichier):

        self.fichier = fichier
        self.structure = []
        self.tool = IMAGE_TOOL

    def parse_file(self):
        """ Generating map from a file. It's a list wich contains
            other lists."""
        with open(self.fichier, "r") as fichier:
            map_structure = []

            for line in fichier:
                line_structure = []

                for sprite in line:
                    if sprite != "\n":
                        line_structure.append(sprite)

                map_structure.append(line_structure)

            self.structure = map_structure

    def insert_tool(self):
        """ map random position for tool and insertion in
        the map structure"""

        item_counter = 0
        while item_counter != len(self.tool):
            # Sometime, the loop below, wich insert the tool
            # in map structure, insert 1 or 2 more tools than expected
            # (len(self.tool) == 3) This loop check the number
            # of item in the map structure et the necessary
            # number before exit

            if item_counter > len(self.tool):
                self.parse_file()
            item_counter = 0
            i = 0

            while i != len(self.tool):
                random_line = random.choice(self.structure)
                random_line_position = self.structure.index(random_line)
                random_sprite = random.randint(0, len(random_line) - 1)
                if random_line[random_sprite] == "0":
                    random_line[random_sprite] = [
                        self.tool[i],
                        random_line_position,
                        random_sprite,
                    ]
                    self.structure[random_line_position] = random_line
                    i += 1

            for line in self.structure:

                for sprite in line:
                    if isinstance(sprite, list):
                        item_counter += 1
