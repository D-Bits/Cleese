""" 
# Directory and file structure to scaffold
# Based on this tutorial: https://www.restapiexample.com/golang-tutorial/golang-mvc-project-structure-without-framework/
-src 
 |_/controllers
 |_/models
 |_/route
 |_/helpers
 |_/config
"""
from os import mkdir, chdir, getenv
from subprocess import run


# Create the base dir for the project
def root(proj_name):
    
    # Change into the directory, specified by GO_PATH 
    go_path = getenv('GOPATH')
    chdir(go_path)
    chdir('src')
    chdir('github.com')
    github_uname = input('Please enter your GitHub username: ')
    chdir(github_uname)

    mkdir(proj_name)
    chdir(proj_name) 


# Create a directory for config vars and/or files
def config():

    mkdir('config')
    open('.env', 'a').write('site : "restapiexample.com"')


# Create the app directory w/ a main.go file
def app():

    mkdir('app')
    open('app/main.go', 'a')
    chdir('app')


# Create dir for controllers
def controllers():

    mkdir('controllers')
    open('controllers/home.go', 'a')


# Create a models dir
def models():

    mkdir('models')
    open('models/types.go', 'a')


# Create a dir for routes
def routes():

    mkdir('routes')
    open('routes/route.go', 'a')

# Create a dir for helpers
def helpers():

    mkdir('helpers')


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



def go_mvc_main():

    user_proj_name = input('Enter a project name: ')

    # Throw exception if user does not enter project name when prompted
    if user_proj_name is None:
        raise Exception('Project name cannot be null!')

    root(user_proj_name)
    config()
    app()
    controllers()
    models()
    routes()
    helpers()
    git()