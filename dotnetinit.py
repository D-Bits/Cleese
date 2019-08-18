"""
Initialize an .NET Core application. 
Requires .NET Core SDK.
"""
from os import mkdir, chdir
from subprocess import run


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
        mvc = run(['dotnet', 'new', 'mvc'])
        mvc.check_returncode()
    elif proj_type == 2:
        web_api = run(['dotnet', 'new', 'webapi'])
        web_api.check_returncode()
        # Create a models dir for webapi
        mkdir('Models')
    elif proj_type == 3:
        console = run(['dotnet', 'new', 'console'])
        console.check_returncode()
    elif proj_type == 4:
        react = run(['dotnet', 'new', 'react'])
        react.check_returncode()
    elif proj_type == 5:
        react_redux = run(['dotnet', 'new', 'reactredux'])
        react_redux.check_returncode()
    else:
        raise Exception('Invalid value!')
    
    open('README.md', 'a')
    # Add a file for automating .NET Core & EF Core tasks
    open('README.md', 'a')


# Install NuGet packages
def packages():

    ef_core = run(['dotnet', 'add', 'package', 'Microsoft.EntityFrameworkCore'])
    ef_core.check_returncode()

    ef_core_design = run(['dotnet', 'add', 'package', 'Microsoft.EntityFrameworkCore.Design'])
    ef_core_design.check_returncode()
    

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


def dotnet_main():
    
    init()
    packages()
    git()
