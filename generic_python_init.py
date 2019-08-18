from subprocess import run
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
    pipenv = run('pip install pipenv')
    pipenv.check_returncode()

    install_pkg_choice = input('Would you like to install a package from Pip, and create a venv(y/n)?: ')

    if install_pkg_choice == 'y':
        pkg_name = input('Enter a Pip package to install: ')
        pkg = run(f'pipenv {pkg_name}')
        pkg.check_returncode()
    elif install_pkg_choice == 'n':
        pass
    else:
        raise Exception('Invalid value entered.')


# Create a main.py file, and a README
def files():

    open('main.py', 'a')
    open('README.md', 'a')


# Initialize a git repo, add, and commit files
def git():

    git_init = run(['git', 'init'])
    git_init.check_returncode()

    git_add = run(['git', 'add', '-A'])
    git_add.check_returncode()

    git_commit = run(['git', 'commit', '-m', 'initial commit'])
    git_commit.check_returncode()

    # Ask the user if they want to do a 'git remote' configuration
    git_remote_choice = input('Would you also like to do a git remote configuration(y/n)?: ')

    if git_remote_choice == "y":
        remote_url = input('Enter the URL of your remote repository: ')
        git_remote = run(['git', 'remote', 'add', 'origin', remote_url])
        git_remote.check_returncode()
    elif git_remote_choice == "n":
        pass
    else:
        input("Invalid value entered. Press enter to exit.")


def generic_py_main():

    project_dir()
    venv()
    files()
    git()