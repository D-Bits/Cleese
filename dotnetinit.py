"""
Initialize an .NET Core application. 
Requires .NET Core SDK.
"""
from os import mkdir, chdir
from subprocess import call


# Create proj dir and scaffold an ASP app
def init():

    choices = {
        '1': 'MVC',
        '2': 'Web API',
        '3': 'Console Program',
        '4': 'ASP, with React',
        '5': 'ASP, with React and Redux',
    }

    proj_name = input('Enter a project name: ')

    if not proj_name:
        raise Exception('Project name cannot be null!')

    mkdir(proj_name)
    chdir(proj_name)

    # Show the user available choices
    for key, val in choices.items():
        
        print(key, val)

    print()

    # Prompt the user to choose a .NET Core project type
    proj_type = int(input('Enter a number, based on the above options: '))

    if proj_type == 1:
        call(['dotnet', 'new', 'mvc'])
    elif proj_type == 2:
        call(['dotnet', 'new', 'webapi'])
        # Create a models dir for webapi
        mkdir('models')
    elif proj_type == 3:
        call(['dotnet', 'new', 'console'])
    elif proj_type == 4:
        call(['dotnet', 'new', 'react'])
    elif proj_type == 5:
        call(['dotnet', 'new', 'reactredux'])
    else:
        raise Exception('Invalid value!')
    
    open('README.md', 'a')


# Install NuGet packages
def packages():

    call(['dotnet', 'add', 'package', 'Microsoft.EntityFrameworkCore'])
    call(['dotnet', 'add', 'package', 'Microsoft.EntityFrameworkCore.SqlServer'])


# Initialize a git repo, add, and commit files
def git():

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


def dotnet_main():
    
    init()
    packages()
    git()
