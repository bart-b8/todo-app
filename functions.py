FILEPATH = r'files\todos.txt'

def get_todos(filepath = FILEPATH):
    """ Return list with all todos. """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath = FILEPATH):
    """ Accepts lists of stirngs. All should end with '\n' 
    and writes it to the file given. 
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
