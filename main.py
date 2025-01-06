from time import strftime

import functions
import time

now = strftime("%b %d %Y %H:%M:%S")
print("HII")
print("it is ",now)
while True:
    User_action=input("Type add,edit,show,complete or exit:")
    User_action=User_action.strip()


    if User_action.startswith("add"):
        todo=User_action[4:]

        todos=functions.get_todos()
        todos.append(todo+"\n")

        functions.write_todos("files/todos.txt",todos)

    elif User_action.startswith("show"):

        todos=functions.get_todos()

        # new_todos=[]
        # for item in todos:
        #     new_item=item.strip('\n')
        #     new_todos.append(new_item)
        # new_todos=[item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif User_action.startswith("edit"):
        try:
            number = int(User_action[5:])
            number = number - 1

            todos=functions.get_todos()

            print("Here is the existing todos:",todos)
            new_todo=input("Enter the Alternate todo:")
            todos[number]=new_todo +"\n"
            functions.write_todos('files/todos.txt', todos)

        except ValueError:
            print("Invalid Command. Please Enter the Valid Command..")
            continue





    elif User_action.startswith("complete"):
        try:
            todos=functions.get_todos()

            for index,item in enumerate(todos):
                item=item.strip('\n')
                row=f"{index+1}-{item}"
                print(row)
            number = int(User_action[9:])
            todos_to_remove=todos[number-1]
            todos.pop(number-1)

            functions.write_todos('files/todos.txt',todos)

            print(f"Todo {todos_to_remove} is removed from the list. Thank You!")
        except IndexError:
            print("There is no item with that number.")
            continue
    elif User_action.startswith("exit"):
        print("Bye")
        break
    else:
        print("Command is not valid.....")
