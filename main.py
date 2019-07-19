from aspinit import asp_main
from djangoinit import django_main
from flaskinit import flask_main
from phpinit import php_main
from goinit import go_main
from generic_python_init import generic_py_main


# User choices for scaffolding
choices = {
    '1': 'Django Project',
    '2': 'Flask Project',
    '3': '.NET Core Project',
    '4': 'PHP Project',
    '5': 'A Golang Project',
    '6': 'A generic Python project.'
}


# Prompt the user to choice a project type to scaffold
if __name__ == "__main__":
    
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
        asp_main()
    elif user_choice == 4:
        php_main()
    elif user_choice == 5:
        go_main()
    elif user_choice == 6:
        generic_py_main()
    else:
        raise Exception('Invalid value.')
