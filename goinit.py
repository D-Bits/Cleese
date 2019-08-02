"""
Initialize a basic Golang project.
"""
from os import mkdir, chdir, getenv
from subprocess import call


def project_dirs(proj_name):

    go_path = getenv('GOPATH')
    chdir(go_path)
    chdir('src')
    chdir('github.com')
    github_uname = input('Please enter your GitHub username: ')
    chdir(github_uname)

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
    open('main.go', 'a')


def go_main():

    user_proj_name = input('Enter a project name: ')
    project_dirs(user_proj_name)
    src()
