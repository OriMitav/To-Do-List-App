import streamlit as st
import functions

todos= functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + "\n" # Creating dictionary contain given value into the key "new_todo"
    todos.append(todo)
    functions.set_todos(todos)

todos = functions.get_todos()

st.title("My todo App")
st.subheader("This is my todo app.")
st.write("This app will improve my productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.set_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label = "",
              placeholder = "Enter new todo...",
              on_change = add_todo,
              key='new_todo')

st.session_state

