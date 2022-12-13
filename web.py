import streamlit as st
import functions

def add_todo():
    todo = st.session_state['new_todo']
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state['new_todo'] = ""



todos = functions.get_todos()

st.title("My Todo App")
st.header("This is my todo app.")
st.subheader("Subheader")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun() #st.rerun() could also be used depending on what works

st.text_input(label="", placeholder="Enter a todo...",
              on_change=add_todo, key='new_todo')

# st.session_state
