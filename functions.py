def get_todos():
    with open('files/todos.txt', 'r') as file_local:
        todos_local = file_local.readlines()
        # file=open('files/todos.txt', 'r')
        # todos=file.readlines()
        # file.close()
        # alternate file handling method is with context manager
    return todos_local

def write_todos(filepath,todos_arg):
    with open(filepath,'w') as file:
        file.writelines(todos_arg)
        # file=open('files/todos.txt', 'w')
        # file.writelines(todos)
        # file.close()


if __name__=="__main__":
    print("hello")
    print(get_todos())