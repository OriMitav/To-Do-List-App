def set_todos(text_file, todos_arg):
    """ Write to do items list into the given text file"""
    with open(text_file, 'w') as file:
        file.writelines(todos_arg)