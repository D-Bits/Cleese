from os import chdir
from dotnetinit import dotnet_main
from djangoinit import django_main
from flaskinit import flask_main
from phpinit import php_main
from goinit import go_main
from generic_python_init import generic_py_main
from nodeexpressinit import node_main


# User choices for scaffolding
choices = {
    '1': 'Django Project',
    '2': 'Flask Project',
    '3': '.NET Core Project',
    '4': 'PHP Project',
    '5': 'A Golang Project',
    '6': 'A generic Python Project.',
    '7': 'A Node/Express Project.'
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
    else:
        raise Exception('Invalid value.')
