"""
Initialize a basic Golang project.
"""
from os import mkdir, chdir
from subprocess import call



def project_dirs(proj_name):

    # Create project base dir
    mkdir(proj_name)
    chdir(proj_name)

    # Create bin, pkg, and src dirs
    mkdir('bin')
    mkdir('pkg')
    mkdir('src')
    chdir('src')


# Create main pkg, with app file
def src():

    mkdir('main')
    chdir('main')
    open('app.go', 'a')


def go_main():

    user_proj_name = input('Enter a project name: ')
    project_dirs(user_proj_name)
    src()