# Code for todo list app.
print("HI!!!  Welcome to the todo list app!!!\n")
todos = []
while True:
    # takes the input about what the user wants to do.
    user_action = input("Select add,show,update,remove,exit:")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter the todo:-") + "\n"

            with open('todos.txt','r') as file:
                file.readlines()

            todos.append(todo)

            #writes the todo into the file todos.txt.
            with open("todos.txt",'w') as file:
                file.writelines(todos)


        case 'show':
            with open("todos.txt","r") as file:
                todos = file.readlines()

           # new_todos = []                # to strip \n from the output.

           # for item in todos:
             #   new_item = item.strip('\n')
             #   new_todos.append(new_item)

           # new_todos = [item.strip('\n') for item in todos]    # list comprehension........another way to strip \n from the output
           # shows the todo list.
            for index,items in enumerate(todos):
                 items = items.title()
                 items = items.strip('\n')
                 better_version = f"{index + 1}-{items}"
                 print(better_version)


        case 'update':
            # updates the existing todo with the new todo.
            number = int(input("Enter the number:"))
            number -= 1

            with open('todos.txt','r') as file:
                file.readlines()

            new_todo = input("Enter the new todo:-")
            todos[number] = new_todo + '\n'

            with open("todos.txt",'w') as file:
                file.writelines(todos)


        case 'remove':
            # removes any todo user wants to remove
            remv_todo = int(input("Enter the no.of todo to remove:-"))

            with open('todos.txt','r') as file:
                file.readlines()

            index = remv_todo - 1
            todo_to_remove = todos[index].strip('\n')

            todos.pop(index)

            with open("todos.txt", 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} has been removed!"
            print(message)


        case 'random':
            print("You entered a wrong command, retry!!")


        case 'exit':
            break

print("Thanks for using my app!!")
print("Bye, have a nice day!!!!")

