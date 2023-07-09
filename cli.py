# Imports
from functions import set_todos


""""""""""""""""""""""""""""""""""""""""""""""""
""" Setups """
""""""""""""""""""""""""""""""""""""""""""""""""

# Constant variables
TEXT_FILE = 'todos.txt'

# Variables
file = open(TEXT_FILE, 'r')
todos = file.readlines()
file.close()

""""""""""""""""""""""""""""""""""""""""""""""""
""" Script """
""""""""""""""""""""""""""""""""""""""""""""""""

while True:
    user_action = input("Type add, show, edit or exit:")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            todos.append(todo)
            set_todos(TEXT_FILE, todos)
        case 'show':
            print_todos = [item.strip('\n') for item in todos]
            for index, item in enumerate(print_todos):
                print(f"{index + 1}. {item}")
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new to do: ") + "\n"
            todos[number] = new_todo
            set_todos(TEXT_FILE, todos)
        case 'complete':
            number = int(input("Number of the todo to compete: "))
            removed = todos[number - 1].strip('\n')
            todos.pop(number - 1)
            set_todos(TEXT_FILE, todos)

            massage = f"The task {removed} was removed successfully"
            print(massage)
        case 'exit':
            break

print("bye!")
