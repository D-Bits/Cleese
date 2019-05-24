"""
Initialize an ASP.NET Core MVC application. 
Requires .NET Core SDK.
"""
from os import mkdir, chdir
from subprocess import call


# Create proj dir and scaffold an ASP app
def init():

    proj_name = input('Enter a project name: ')

    if not proj_name:
        raise Exception('Project name cannot be null!')

    mkdir(proj_name)
    chdir(proj_name)

    call('dotnet new mvc')
    open('README.md', 'a')


# Install NuGet packages
def packages():

    call('dotnet add package Microsoft.EntityFrameworkCore')
    call('dotnet add package Microsoft.EntityFrameworkCore.SqlServer')


def git():

    call('git init')
    call('git add -A')
    call('git commit -m "initial commit"')


if __name__ == "__main__":
    
    init()
    packages()
    git()

