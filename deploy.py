"""
Run this file automate compiling of execuatables.
"""
from subprocess import call
from os import getenv
from shutil import move


# Run cmds to compile for both Windows & Linux
def compile():

    call(['pyinstaller', 'main.py', '-F', '-n', 'scaffold_projects'])
    call(['wsl', 'pyinstaller', 'main.py', '-F', '-n', 'scaffold_projects'])


# Move all executables to a specific dir after being created
def move_executables():

    # Default location, created by PyInstaller
    src_dir = getenv('SCAFF_DIST')
    # Define a location to move all executables to 
    target_dir = getenv('EXEC_DIR')

    move(src_dir, target_dir)


def deploy():

    compile()
    move_executables()


deploy()
