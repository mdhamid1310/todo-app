import  functions
import FreeSimpleGUI as sg



#
# from cli import new_todo

label=sg.Text("Type in a todo")
input_box=sg.InputText(tooltip="Enter a todo",key="todo")
add_button=sg.Button("Add")
# listbox=sg.Listbox(functions.get_todos())
# edit_button=sg.Button("Edit")

window=sg.Window("My Todo App",
                 layout=[[label],[input_box,add_button]],
                 font=('Helvetica',20))

while True:
    event,values=window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos=functions.get_todos()
            new_todo=values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()