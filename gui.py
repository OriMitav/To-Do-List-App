import functions
import PySimpleGUI as sg

lable= sg.Text("Type in a to do")
input_box=sg.InputText(tooltip="Enter to do", key="todo")
add_button=sg.Button("Add")
edit_button =sg.Button("Edit")
list_box=sg.Listbox(values=)

window=sg.Window('My to do app',
                 layout=[[[lable],input_box,add_button,edit_button]],
                 font=('Helvetica',20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo']+"\n"
            todos.append(new_todo)
            functions.set_todos(todos)
        case sg.WINDOW_CLOSED:
            break
window.close()
