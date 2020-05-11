#!/usr/bin/python3
# -*- coding: Utf-8 -*

from cx_Freeze import setup, Executable

# calling setup fonction
setup(
    name = "Mac Gyver : escape from the maze",
    version = "1.0",
    description = "Votre programme",
    executables = [Executable("votre_script.py")],
)
