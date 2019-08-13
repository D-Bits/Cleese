"""
Run this file automate compiling of execuatables.
"""
from subprocess import call
from os import getenv
from shutil import move


# Run cmds to compile for both Windows & Linux
call(['pyinstaller', 'main.py', '-F', '-n', 'scaffold_projects'])
