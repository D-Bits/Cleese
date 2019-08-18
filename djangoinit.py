from subprocess import run
from os import chdir, mkdir


def create_root():

    dir_name = input("Enter a name for the project base dir: ")

    mkdir(dir_name)
    chdir(dir_name)

    """Create virtualenv w/ Pipenv, and install packages"""
    
    # Install pipenv, if it is not already installed
    pipenv = run(['pip', 'install', 'pipenv'])
    pipenv.check_returncode()

    django = run(['pipenv', 'install', 'django'])
    django.check_returncode()

    # Ask the user if they also want to install DRF
    drf_choice = input('Would you also like to install Django REST Framework (y/n)?: ')
    if drf_choice == 'y':
        drf = run(['pipenv', 'install', 'djangorestframework'])
        drf.check_returncode()
    elif drf_choice == 'n':
        pass
    else:
        raise Exception('Invalid value entered.')
    
    # Prompt the user to specify what DBMS they want to use
    db_pkg_choice = input('Specify a database connector (ex:"psycopg2", "mysqlclient", etc): ')
    if not db_pkg_choice:
        raise Exception('Must specify a db connector!')
    db_pkg = run(['pipenv', 'install', db_pkg_choice])
    db_pkg.check_returncode()

    open('README.md', 'a')

    # Add a "tasks.py" file to the base dir to automate execute of manage.py tasks
    open('tasks.py', 'a')


""" Prompt the user for a project name, then
Run the django-admin startproject cmd  """
def start_project():
    
    proj_name = input("Enter a project name: ")

    # Throw an exception is proj_name is null
    if not proj_name:
        raise Exception('Project name cannot be null!')

    mkdir(proj_name)
    chdir(proj_name)

    dj_admin = run(['django-admin', 'startproject', proj_name])
    dj_admin.check_returncode()

    chdir(proj_name)


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


# Add an app to the project
def create_app():

        app_name = input("Enter a name for your first Django project app: ")

        # Throw an exception is app_name is null
        if not app_name:
            raise Exception('App name cannot be null!')

        start_app = run(['django-admin', 'startapp', app_name])
        start_app.check_returncode()

        # Change into the app dir, and create a "tests" dir for unit testing
        chdir(app_name)

        mkdir('tests')
        open('tests/__init__.py', 'a')
        open('tests/test_models.py', 'a')
        open('tests/test_views.py', 'a')
        open('tests/test_forms.py', 'a')

        # Go up to parent dir
        chdir('..')

    
def django_main():

    create_root()
    start_project()
    create_app()
    git()
        