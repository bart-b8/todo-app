import functions
import PySimpleGUI as sg
import time

# A preview is avalable under sg.theme_previewer() OR on google: 'PySimpleGUI themes'
sg.theme("DarkTanBlue")

label = sg.Text("Type in a to-do")
clock_lbl = sg.Text("", key='clock')
input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button(size=2, image_source="add.png", key='Add', mouseover_colors="LightBlue2",
                       tooltip="Add Todo")
list_box = sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button('Exit')

window = sg.Window('My To-Do App', 
                   layout=[[label, clock_lbl], [input_box, add_button], [list_box, edit_button, complete_button],
                           [exit_button]], 
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(event)
    print(values)

    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values['todo'] + "\n")
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            try:
                todo = values['todos'][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo)
                todos[index] = new_todo + '\n'
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("please select item first", font=("Helvetica", 20))

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update('')
            except IndexError:
                sg.popup("please select item first", font=("Helvetica", 20))

        case 'todos':
            try:
                window['todo'].update(value=values['todos'][0])
            except IndexError:
                continue

        case 'Exit':
            break

        case sg.WIN_CLOSED:
            break

window.close()

