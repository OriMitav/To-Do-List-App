import functions
import PySimpleGUI as sg

lable= sg.Text("Type in a to do")
input_box=sg.InputText(tooltip="Enter to do")
add_button=sg.Button("Add")

window=sg.Window('My to do app', layout=[[[lable],input_box,add_button]])
window.read()
window.close()
