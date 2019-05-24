"""
CAUTION: Not yet working. 
Configure a Ruby on Rails dev environment, w/ support 
for PostgreSQL.
"""

from subprocess import call
from os import chdir


# Update packages and install dependenices for Ruby
def updates():

    call('sudo apt update')
    call('sudo apt install autoconf bison build-essential libssl-dev libyaml-dev libreadline6-dev zlib1g-dev libncurses5-dev libffi-dev libgdbm5 libgdbm-dev')


# Install and config rbenv
def rbenv():

    call('git clone https://github.com/rbenv/rbenv.git ~/.rbenv')
    call('echo "export PATH="$HOME/.rbenv/bin:$PATH"" >> ~/.bashrc')
    call('echo "eval "$(rbenv init -)"" >> ~/.bashrc')
    call('source ~/.bashrc')
    call('type rbenv') # Verify rbenv is installed properly 


# Install necessary gems
def gems():

    call('gem install bundler') # Install gem bundler
    call('gem install rails') # Install Rails
    call('gem install pg') # Install support for PostgreSQL 


# Create a new Rails project
def project():

    proj_name = input("Enter a project name: ")
    
    if not proj_name:
        raise Exception('Project name cannot be null!')

    call(['rails new'], [proj_name], ['--database=postgresql'])
    chdir(proj_name) 


# Initalize a git repo, add, and commit files
def git():

    call('git init')
    call('git add -A')
    call('git commit -m "Initial commit"')


def main():
    
    #updates()
    rbenv()
    gems()
    project()
    git()


main()