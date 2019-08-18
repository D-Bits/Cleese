"""
Scaffold together a basic Flask project, meant to 
be run in the project's base directory. Uses Pipenv, 
but does not need to be pre-installed to run.

# Packages to be installed

* Flask
* Flask-SQLAlchemy
* Flask-WTForms
* Flask-Security 

# Project structure
-package_name
 |__/templates
 |   |_layout.html
 |__/models
 |__/static
 |   |__/css
 |   |   |_main.css
 |   |__/js
 |   |   |_main.js
 |   |__/img
 |__/tests
 |__app.py
"""
from os import mkdir, chdir
from subprocess import run


# Create the parent dir for the project, and cd into it
def project_root():

    proj_name = input('Enter a project name: ')

    if not proj_name:
        raise Exception('Package name cannot be null!')

    mkdir(proj_name)
    chdir(proj_name)
    open('app.py', 'a')
    open('README.md', 'a')
    # Create a file to automate flask tasks
    open('tasks.py', 'a')

    # Export a local environment var, so 'flask run' can be used (not yet working)
    #call(['export', 'FLASK_APP=app.py'])


# Create a virtualenv w/ pipenv, and install packages inside it
def pipenv():

    # Install pipenv, if it is not already installed
    pipenv = run(['pip', 'install', 'pipenv'])
    pipenv.check_returncode()

    flask = run(['pipenv', 'install', 'flask'])
    flask.check_returncode()

    sql_alchemy = run(['pipenv', 'install', 'flask-sqlalchemy'])
    sql_alchemy.check_returncode()

    flask_wtf = run(['pipenv', 'install', 'flask-wtf'])
    flask_wtf.check_returncode()

    flask_security = run(['pipenv', 'install', 'flask-security'])
    flask_security.check_returncode()

    alembic = run(['pipenv', 'install', 'flask-alembic'])
    alembic.check_returncode()
    

    # Prompt the user to specify what DBMS they want to use
    db_pkg_choice = input('Specify a database connector (ex:"psycopg2", "mysqlclient", etc): ')
    if not db_pkg_choice:
        raise Exception('Must specify a db connector!')

    db_pkg = run(['pipenv', 'install', db_pkg_choice])
    db_pkg.check_returncode()


# Create project package directory
def create_pkg():
    
    # Prompt the user for a package name
    pkg_name = input('Enter a name for your Flask package: ')
   
    # Throw an exception is package name is null
    if not pkg_name:
        raise Exception('Package name cannot be null!')

    mkdir(pkg_name) 
    chdir(pkg_name) # Change into the package directory
    open('models.py', 'a')
    open('forms.py', 'a')
    open('routes.py', 'a')
    open('__init__.py', 'a')


# Create templates directory
def create_templates():

    mkdir('templates') 
    # Create a layout template in dir for other templates to inherit from
    open('templates/layout.html', 'a') 
    open('templates/index.html', 'a') 


# Create static files directory    
def create_static():

    mkdir('static')
    # Create CSS dir and main.css file, if it doesn't already exist
    mkdir('static/css')
    open('static/css/main.css', 'a') 
    # Create JS dir and main.js file, if it doesn't already exist
    mkdir('static/js') 
    open('static/js/main.js', 'a')
    # Create an images dir
    mkdir('static/img') 


# Create directory for unit tests
def create_tests():

    mkdir('tests')
    open('tests/test_models.py', 'a')
    open('tests/test_routes.py', 'a')


# Initialize git repo, add+commit files
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


def flask_main():

    project_root()
    pipenv()
    create_pkg()
    create_templates()
    create_static()
    create_tests()
    git()


