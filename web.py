import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    todo = str(todo).capitalize()
    todos.append(todo + "\n")
    functions.store_todos(todos)

st.title("My To-do App")
st.subheader("This is my to-do list:")
st.write("This app is to improve your <b>productivity</b>.", unsafe_allow_html=True)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.store_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label=" ", placeholder="Add new to-do...", on_change=add_todo, key="new_todo")