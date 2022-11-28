FILEPATH = r'files\todos.txt'

import os

if not os.path.isdir(os.path.split(FILEPATH)[0]):
    os.mkdir(os.path.split(FILEPATH)[0])
if not os.path.exists(FILEPATH):
    with open(FILEPATH, 'w') as file:
        pass

def get_todos(filepath = FILEPATH):
    """ Return list with all todos. """
    with open(filepath, 'r') as file_local:
        # todos_local = file_local.readlines()
        todos_local = file_local.read().splitlines() #Removes \n from each line
    return todos_local

def write_todos(todos_arg, filepath = FILEPATH):
    """ Accepts lists of stirngs. All should end with '\n' 
    and writes it to the file given. 
    """
    todos_arg = [arg + '\n' for arg in todos_arg]
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
