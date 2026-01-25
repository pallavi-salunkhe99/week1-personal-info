# Q 3.	Make a shopping list manager with add/remove functionality.

print("\n")
print("*"*70)
print("\t\t\tShopping List Manager")
print("*"*70)
print("\n")

list=[]
while True:
    print("************* User choice Menu  *************")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    print()
    ch=int(input("Enter Your Choice:"))
    print()
    if(ch == 1):
        item=input("Enter Item name to add in List: ")
        list.append(item)
        print("Item added in list sussfully..!\n")
    elif(ch == 2):
        list.pop()
        print("Item deleted in list sussfully..!\n")
    elif(ch == 3):
        print("List items are: ", list ,"\n")
    elif(ch == 4):
        break
    else:
        print("wrong choice..! please try again.\n")

print()
print("-"*70)
print("\t\tThanks for visiting me My Python Program..!")
print("-"*70)
print()

