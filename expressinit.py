"""
CAUTION: Not yet working. 
Scaffold together a Node.js/Express Application.
"""
from os import mkdir, chdir, environ
from sys import stdout
from subprocess import call


# Create project root dir
def create_root():

    uinput = input('Enter a project name: ')
    mkdir(uinput)
    chdir(uinput)

    # Create files in root directory
    open('app.js', 'a')
    open('README.md', 'a')


def controllers():

    mkdir('controllers')


def models():

    mkdir('models')


def views():

    mkdir('views')
    open('views/index.hbs', 'a')
    open('views/layout.hbs', 'a')


# Create routes dir
def routes():

    mkdir('routes')
    open('routes/index.js', 'a')


# Create a dir for unit tests
def tests():

    mkdir('tests')
    open('tests/model_tests.js', 'a')
    open('tests/controller_tests.js', 'a')


# Install packages from NPM
def packages():

    call(['npm', 'install', 'handlebars'])
    call(['npm', 'install', 'express'])
    call(['npm', 'install', 'mocha'])
    call(['npm', 'init'])


# Initialize a git repo, commit & add all files created
def git():

    call(['git', 'init'])
    call(['git', 'add', '-A'])
    call(['git', 'commit', '-m', '"initial commit"'])


def node_main():

    create_root()
    packages()
    controllers()
    models()
    views()
    routes()
    tests()
    git()

node_main()