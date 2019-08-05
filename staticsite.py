
# Scaffold a simple, static website
"""
# Directory and file structure to scaffold
-src
 |__/css
 |  |_main.css
 |__/img
 |__/js
 |    |_main.js
 |__index.html
 |__README.md
"""
from os import mkdir, chdir
from subprocess import call


# Create project base directory
def base_dir(dir_name):

    mkdir(dir_name)
    chdir(dir_name)
    open('index.html', 'a')
    open('README.md', 'a')

# Create a dir for CSS files
def css():

    mkdir('css')
    open('css/main.css', 'a')


# Create a dir for images
def img():

    mkdir('img')


# Create a file for JS files
def js():

    mkdir('js')
    open('js/main.js', 'a')


# Initialize a git repo, commit & add all files created
def git():

    call(['git', 'init'])
    call(['git', 'add', '-A'])
    call(['git', 'commit', '-m', '"initial commit"'])

    # Ask the user if they want to do a 'git remote' configuration
    git_remote = input('Would you also like to do a git remote configuration(y/n)?: ')

    if git_remote == "y":
        remote_url = input('Enter the URL of your remote repository: ')
        call(['git', 'remote', 'add', 'origin', remote_url])
    elif git_remote == "n":
        pass
    else:
        input("Invalid value entered. Press enter to exit.")


def static_main():

    proj_dir = input('Enter a name for your website: ')
    
    base_dir(proj_dir)
    css()
    img()
    js()
    git()