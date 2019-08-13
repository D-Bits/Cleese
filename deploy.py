"""
Run this file automate compiling of execuatables.
"""
from subprocess import call


# Run cmds to compile for both Windows & Linux
call(['pyinstaller', 'main.py', '-F', '-n', 'scaffold_projects'])
call(['wsl', 'pyinstaller', 'main.py', '-F', '-n', 'scaffold_projects'])