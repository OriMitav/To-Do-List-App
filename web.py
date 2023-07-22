import streamlit as st
import functions

todos= functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    functions.set_todos(todos)

todos = functions.get_todos()

st.title("My todo App")
st.subheader("This is my todo app.")
st.write("This app will improve my productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label = "",
              placeholder = "Enter new todo...",
              on_change = add_todo,
              key='new_todo')
