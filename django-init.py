"""
Create a Django project, in 
a virtualenv with psycopg2 installed. 

"""
from subprocess import call
from os import chdir, mkdir

def create_root():

    dir_name = input("Enter a name for the project base dir: ")

    mkdir(dir_name)
    chdir(dir_name)

    """Create virtualenv w/ Pipenv, and install packages"""
    # Make sure pip is up-to-date
    call('python -m pip install --upgrade pip')
    # Install pipenv, if it is not already installed
    call('pip install pipenv')
    call('pipenv install django')
    call('pipenv install psycopg2')

    open('README.md', 'a')


""" Prompt the user for a project name, then
Run the django-admin startproject cmd  """
def start_project():
    
    proj_name = input("Enter a project name: ")

    # Throw an exception is proj_name is null
    if not proj_name:
        raise Exception('Project name cannot be null!')

    mkdir(proj_name)
    chdir(proj_name)

    call('django-admin.exe startproject ' + proj_name)
    
    


"""
Initialize empty git repo, then add + commit all project files
"""
def git():

    call('git init')
    call('git add -A')
    call('git commit -m "initial commit" ')


# Add an app to the project
def create_app():

        app_name = input("Enter a name for your first Django project app: ")
        
        # Throw an exception is app_name is null
        if not app_name:
            raise Exception('App name cannot be null!')

        call('django-admin.exe startapp ' + app_name)

    
if __name__ == "__main__":

    create_root()
    start_project()
    create_app()
    git()
        