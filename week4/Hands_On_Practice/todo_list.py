# 5. Build a to-do list that persists between program runs.

print()
print("*"*90)
print("\t\t\t\tTo-do List")
print("*"*90,"\n")

def display_menu():
    print("----------------  Selection Menu  ----------------\n")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit\n")

def add_task():
    print("\n==========  Start Adding Task  ==========\n")
    title = input("Enter Task title: ")
    task_num = int(input("Enter how many task: "))
    tasks = []

    for i in range(1,task_num+1):
        task=input(f"Enter Task {i}: ")
        tasks.append(task)

    with open("todo.txt","a") as f:
        f.write("\nTask Title: "+ title + "\n")
        for i, task in enumerate(tasks,start=1):
            f.write(f"{i}.{task}\n")
    print("\nTask added succsfully.\n")
    

def view_task():
    print("\n\n===============  View all To Do List tasks  ===============\n")
    try:
        with open("todo.txt","r") as f:
            data = f.read()
            if data.strip() == "":
                print("\nNo task found.\n")
            else:
                print("\n===============  Your To Do List  ===============")
                print(data)
                print("\n===============-------------------===============\n")
    except FileNotFoundError:
        print("No to-do list found.")

while True:

    display_menu()
    ch = int(input("Enter your choice: "))

    if(ch == 1):
        add_task()

    elif(ch == 2):
        view_task()

    elif(ch == 3):
        break

    else:
        print("\n Invalid choice.. plese try again. \n")

print()
print("*"*90)
print("\t\t\t Thanks for visiting my quiz game")
print("*"*90,"\n")
