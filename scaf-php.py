"""
# Directory and file structure to scaffold
-src
 |__/admin
 |   |_index.php 
 |__/css
 |   |_main.css
 |__/images
 |__/includes
 |__/js
 |  |_main.js
 |
 |__index.php
"""
from os import mkdir, chdir
from subprocess import call

# Create project's base directory
def root():

    proj_name = input('Enter a project name: ')

    # Throw exception if user does not enter project name when prompted
    if proj_name is None:
        raise Exception('Project name cannot be null!')
    
    mkdir(proj_name)
    chdir(proj_name) 
    open('index.php', 'a')
    open('README.md', 'a')
    

# Initialize a git repo, add and commit all files created
def git():

    call('git init')
    call('git add -A')
    call('git commit -m "Initial commit"')


# Create the admin dir, with an index file
def admin():

    mkdir('admin')
    open('admin/index.php', 'a')


# Create a directory for stylesheets, with a main.css
def css():

    mkdir('css')
    open('css/main.css', 'a')


# Create a directory for stylesheets, with a main.css
def images():

    mkdir('images')


# Create a directory for includes, with a header, and footer include
def includes():

    mkdir('includes')
    open('includes/header.php', 'a')
    open('includes/footer.php', 'a')


# Create a directory for js files
def js():

    mkdir('js')
    open('js/main.js', 'a')


def main():

    root()
    admin()
    css()
    images()
    includes()
    js()
    git()


main()