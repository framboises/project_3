#!/usr/bin/python3
# -*- coding: Utf-8 -*

import random

IMAGE_TOOL = ["images/sewing_needle.png", "images/tube.png", "images/ether.png"]

class Map:
    """ Map generator """

    def __init__(self, fichier):

        self.fichier = fichier
        self.structure = 0

    def initiate(self):
        """ Generating map from a file. It's a list wich contains other lists."""
        with open(self.fichier, "r") as fichier:
            map_structure = []

            for line in fichier:
                line_structure = []

                for sprite in line:
                    if sprite != '\n':
                        line_structure.append(sprite)

                map_structure.append(line_structure)

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




# Testing code for prompt
map = Map('level_1')
map.initiate()
print("Hello")
print(map.structure)
