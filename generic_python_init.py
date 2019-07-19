from subprocess import call
from os import mkdir, chdir 

"""
Create a (mostly) empty Python project, with a virtualenv, using
Pipenv. 
"""


# Create the base directory for the project
def project_dir():

    """ Prompt the user to enter a project name,
    and create a directory based on it. """
    dir_name = input('Enter a name for your project: ')
    mkdir(dir_name)
    chdir(dir_name)


# Create a virtualenv, using Pipenv
def venv():

    # Install Pipenv, if its not already
    call('pip install pipenv')

    install_pkg = input('Would you like to install a package from Pip, and create a venv(y/n)?: ')

    if install_pkg == 'y':
        pkg = input('Enter a Pip package to install: ')
        call(f'pipenv {pkg}')
    elif install_pkg == 'n':
        pass
    else:
        raise Exception('Invalid value entered.')


# Create a main.py file, and a README
def files():

    open('main.py', 'a')
    open('README.md', 'a')


# Initialize a git repo, add, and commit files
def git():

    call('git init')
    call('git add -A')
    call('git commit -m "initial commit"')


def generic_py_main():

    project_dir()
    venv()
    files()
    git()