from functions import *
import time

while True :

    user_action = input("Type 'add', 'show', 'edit', 'complete' or 'exit': ").lower().strip()
    # action_list = user_action.split()

    if user_action.startswith("add"):
        if len(user_action) <= 4:
            todo = input("Enter a todo: ")
        else:
            todo = user_action[4:]

        todos = get_todos()
        todos.append(todo.capitalize())

        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()
        for index, item in enumerate(todos):
            print("{}. {}".format(index+1, item))

    elif user_action.startswith("edit"):
        try:
            if len(user_action)<=5:
                print("overview of the todo's")
                todos = get_todos()
                for index, item in enumerate(todos):
                    print("{}. {}".format(index + 1 , item))
                number = int(input("Number of the todo to edit: "))-1
            else:
                number = int(user_action[5:]) - 1
            todos[number] = input("New version of todo {}: ".format(number+1))
            write_todos(todos)
            print('Got it!')
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            if len(user_action)<=9:
                print("overview of the todo's")
                todos = get_todos()
                for index, item in enumerate(todos):
                    print("{}. {}".format(index + 1 , item))
                number = int( input("Number of todo completed: "))-1
            else:
                number = int(user_action[9:])-1
            todos.pop(number)
            write_todos(todos)

            print("Todo is deleted")
        except IndexError:
            print("There is no item with that number")
            continue
    elif user_action.startswith("exit"):
        break
    else: 
        print("Command is not recognized")

print('bye')


