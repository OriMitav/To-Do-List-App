import time
import datetime

import functions
import PySimpleGUI as sg

clock = sg.Text('', key='clock')
lable = sg.Text("Type in a to do")
input_box = sg.InputText(tooltip="Enter to do", key="todo")

sg.theme('DarkTeal11')
""" Editing the GUI visual"""
# Buttons
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
# List box
list_box = sg.Listbox(values=functions.get_todos(),
                      key='todos',
                      enable_events=True,
                      size=[45, 10])
# Presenting
window = sg.Window('My to do app',
                   layout=[[clock],
                           [lable],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))
""" GUI logic """
while True:
    event, values = window.read(timeout = 200)
    window['clock'].update(value=datetime.datetime.now().strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.set_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.set_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item" , font=("helvetica", 20))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.set_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item", font=("helvetica", 20))
        case "Exit":
            break
        case 'todos':
            window['todo'].update(values['todos'][0])
        case sg.WINDOW_CLOSED:
            break
window.close()

