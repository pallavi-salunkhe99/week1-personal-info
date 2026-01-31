# 7. Create functions with different parameter types.

# welcome message
print()
print("*" *90)
print("\t\t\tFunctions with Different parameter Types")
print("*" *90,"\n")

while True:
    print("**** Menu ****\n")
    print("1. No parameters")
    print("2. One parameter")
    print("3. Multiple parameters")
    print("4. Different data types")
    print("5. Exit\n")

    ch=int(input("Enter your choice: "))
    if(ch == 1):
        def hello_world():
            print("\nHello World. \n")
        
        hello_world()
    
    elif(ch == 2):
        def is_even_odd(number):
            if(number %2 == 0):
                print("\nIs EVEN Number.\n")
            else:
                print("\nIs ODD Number.\n")

        number=int(input("Enter a number: "))
        is_even_odd(number)
        
    
    elif(ch == 3):
        def is_greatr_not(a, b, c):
            if(a > b and a > c):
                print("\nA is greater number.\n")
            elif(b > a and b > c):
                print("\nB is greater number.\n")
            else:
                print("\nC is greater number.\n")
        
        a=int(input("Enter a number 1: "))
        b=int(input("Enter a number 2: "))
        c=int(input("Enter a number 3: "))
        is_greatr_not(a, b, c)
        

    elif(ch == 4):
        def diff_datatype(id,name,marks):
            print("\nID |\t Name |\t Marks \n")
            print(id," |",name," |",marks,"\n")
            

        id=int(input("Enter ID: "))
        name=input("Enter Name: ")
        marks=float(input("Enter Marks: "))
        diff_datatype(id,name,marks) 
    

    elif(ch == 5):
        break

    else:
        print("\nInvalid choice.. please try again.\n")
        
    
# good bye message
print()
print("-"*90)
print("\t\t\t  Thanks for visiting my Function CODE.")
print("-"*90,"\n")

