"""
# Directory and file structure to scaffold
-src
 |__/admin
 |  |_index.php
 |  |_login.php
 |  |_logout.php
 |__/includes
 |  |_header.php
 |  |_footer.php
 |__/static
 |  |_/css
 |  | |_main.css
 |  |_/images
 |  |_/js
 |    |_main.js
 |__index.php
"""
from os import mkdir, chdir
from subprocess import call


# Create project's base directory
def root(proj_name):
    
    mkdir(proj_name)
    chdir(proj_name) 
    open('index.php', 'a')
    open('README.md', 'a')
    

# Initialize a git repo, add and commit all files created
def git():

    call(['git', 'init'])
    call(['git', 'add', '-A'])
    call(['git', 'commit', '-m', 'Initial commit'])


# Create the admin dir, with an index file
def admin():

    mkdir('admin')
    open('admin/index.php', 'a')
    open('admin/login.php', 'a')
    open('admin/logout.php', 'a')


# Create directory for config files
def config():

    mkdir('config')
    open('config/config.php', 'a')
    open('config/db.php', 'a')


# Create a directory for static files (CSS, JS, Images)
def static():

    # Create CSS dir
    mkdir('static')
    mkdir('static/css')
    open('static/css/main.css', 'a')

    # Create images dir
    mkdir('static/images')

    # Create JS dir
    mkdir('static/js')
    open('static/js/main.js', 'a')


# Create a directory for includes, with a header, and footer include
def includes():

    mkdir('includes')
    open('includes/header.php', 'a')
    open('includes/footer.php', 'a')


def php_main():

    user_proj_name = input('Enter a project name: ')

    # Throw exception if user does not enter project name when prompted
    if user_proj_name is None:
        raise Exception('Project name cannot be null!')

    root(user_proj_name)
    admin()
    config()
    static() 
    includes()
    git()
