# Project 3 - Mac Gyver

## Description

Imagine a 2D labyrinth in which MacGyver was trapped. The exit is owned by a bodyguard whose hairstyle would make Tina Turner turn pale. To distract him, you need to gather the following elements (scattered in the labyrinth): a sewing needle, a small plastic tube and ether. They will allow MacGyver to create a syringe and put the guard to sleep to escape the labyrinth.

### Features

1. There is only one level.
2. The structure (departure, location of walls, exit), must be saved in a file for easy modification if necessary.
3. MacGyver will be controlled by the directional keys on the keyboard.
4. The objects will be randomly distributed in the labyrinth and will change location if the user closes the game and restart it.
5. The game window will be a square that can display 15 sprites in length. MacGyver will therefore have to move from box to box, with 15 boxes along the length of the window!
6. It will recover an object simply by moving on it. This will increment a displayed counter.
7. The program stops only if MacGyver has recovered all the objects and found the exit from the labyrinth.
8. If he does not have all the objects and he appears before the guard, he dies (life is cruel for the heroes).
9. The program will be standalone, ie it can be run on any computer.

### Installation

* Before running the game, please install requirements.
* Execute`pip install -r requirements.txt`
* From the source folder  
* Execute `python -m macgyver`

---------------

## Release v 1.2 - 14/05/2020

**Technical modification, no new features :**
* Create a python module standalone running
* Application of the strict **PEP8** on the code with flake8
* New files distribution tree 
* Remove pygame use in the character classe
* Using action verb for methods
* Installation instruction in readme

---------------

## Release v 1.1 - 11/05/2020

**New features :**
* New counter for the item collect with a backpack display
* Move 2 features from main to classes

---------------

## Release v 1.0 - 11/05/2020

Final release with all fixed issues

**ENJOY IT**

---------------

## Release beta v 2.0 - 10/05/2020

**Corrections des problèmes de la beta 1.0** :
* New distribution for classes in package file
* Fix all issue about tools and tools insertion in the maze
* Reduction of the main feature but we can do better


**Still to be done:**
* Further decrease the main function
* Write technical documentation
* Move control of walls and collisions from the map class to the character class

---------------

## Release beta 1.0 - 08/05/2020

**This beta version already allows the game to work in graphical version:**
* Import and use of the pygame module
* Generation of a card based on a file
* Random insertion of tools necessary for success
* Possibility to move the character in the labyrinth
* Possibility for the character to recover the objects but the objects are reversed upon recovery
* Exit from the labyrinth with control over the number of objects recovered for the victory
* Victory or defeat screen

**Still to be done:**
* Problem on classes to be distributed in several files
* Problem on the recovery of the tools, when a tool is taken it can be reversed with another tool present in the labyrinth => *work track on the insertion of a list*
* Main () function too important need to divide the game loop into two loops: 1 / home screen loop and labyrinth loop


