import streamlit as st
import functions

todos = functions.get_todos()
st.text(type(todos))
st.text(type(todos[0]))

st.title("My Todo App")
st.header("This is my todo app.")
st.subheader("Subheader")
st.write("This app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)
