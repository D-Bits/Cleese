from os import chdir
from subprocess import call
from dotnetinit import dotnet_main
from djangoinit import django_main
from flaskinit import flask_main
from phpinit import php_main
from goinit import go_main
from generic_python_init import generic_py_main
from nodeexpressinit import node_main
from staticsite import static_main
from gomvc import go_mvc_main


# User choices for scaffolding
choices = {
    '1.': 'Django project',
    '2.': 'Flask project',
    '3.': '.NET Core project',
    '4.': 'PHP project',
    '5.': 'Golang project',
    '6.': 'Generic Python project.',
    '7.': 'Node/Express project.',
    '8.': 'Simple, static website.',
    '9.': 'Golang MVC web project.'
}


# Prompt the user to choice a project type to scaffold
if __name__ == "__main__":
    
    dir_path = input('Enter the path of the directory where you store your projects (Ex: /home/documents/projects): ')
    chdir(dir_path)

    print() # Blank line for readability

    for key, val in choices.items():
        
        print(key, val)

    print()

    user_choice = int(input('Enter an above interger to specify a project type: '))

    if user_choice == 1:
        django_main()
    elif user_choice == 2:
        flask_main()
    elif user_choice == 3: 
        dotnet_main()
    elif user_choice == 4:
        php_main()
    elif user_choice == 5:
        go_main()
    elif user_choice == 6:
        generic_py_main()
    elif user_choice == 7:
        node_main()
    elif user_choice == 8:
        static_main()
    elif user_choice == 9:
        go_mvc_main()
    else:
        raise Exception('Invalid value.')
