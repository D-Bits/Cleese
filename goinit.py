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

def git():

    chdir('..')
    chdir('..')
    call(['git', 'init'])
    call(['git', 'add', '-A'])
    call(['git', 'commit', '-m', 'initial commit'])

    # Ask the user if they want to do a 'git remote' configuration
    git_remote = input('Would you also like to do a git remote configuration(y/n)?: ')

    if git_remote == "y":
        remote_url = input('Enter the URL of your remote repository: ')
        call(['git', 'remote', 'add', 'origin', remote_url])
    elif git_remote == "n":
        pass
    else:
        input("Invalid value entered. Press enter to exit.")


def go_main():

    user_proj_name = input('Enter a project name: ')
    project_dirs(user_proj_name)
    src()
