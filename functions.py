#Set up defoult values
TEXT_FILE = 'todos.txt'

def get_todos(text_file = TEXT_FILE):
    """ Read a text file and return the list of to do items"""
    with open(text_file, 'r') as file:
        todos= file.readlines()
    return todos

def set_todos(todos_arg, text_file=TEXT_FILE):
    """ Write to do items list into the given text file"""
    with open(text_file, 'w') as file:
        file.writelines(todos_arg)