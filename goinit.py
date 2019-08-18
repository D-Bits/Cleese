"""
Initialize a basic Golang project.
"""
from os import mkdir, chdir, getenv
from subprocess import run


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


def go_main():

    user_proj_name = input('Enter a project name: ')
    project_dirs(user_proj_name)
    src()
