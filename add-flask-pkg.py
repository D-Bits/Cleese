"""
Add a new package to an existing Flask application. 
"""
from os import mkdir, chdir


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


create_pkg()