file = open('todos.txt', 'r')

# Declarations
todos = file.readlines()
file.close()

while True:
    user_action = input("Type add, shoe, edit or exit:")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show':
            print_todos = [item.strip('\n') for item in todos]
            for index, item in enumerate(print_todos):
                print(f"{index + 1}. {item}")
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new to do: ")+ "\n"
            todos[number] = new_todo

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'complete':
            number = int(input("Number of the todo to compete: "))
            removed= todos[number - 1].strip('\n')
            todos.pop(number - 1)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()

            massage = f"The task {removed} was removed successfully"
            print(massage)
        case 'exit':
            break

print("bye!")
