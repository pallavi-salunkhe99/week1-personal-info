# 6.Practice string methods like upper(), lower(), split(), strip().


# welcome message
print()
print("*" *90)
print("\t\t\t\tString Methods Example")
print("*" *90,"\n")

while True:
    print("******* Operation Menu of string Methods *******\n")
    print("1. Upper()")
    print("2. lower()")
    print("3. split()")
    print("4. strip()")
    print("5. Exit","\n")

    ch=int(input("Enter Choice: "))
    def is_string():
       str=input("Enter String: ")
       return str
    
    if(ch == 1):
        str=is_string()
        print("\nupper method: ",str.upper(),"\n")
    
    elif(ch == 2):
        str=is_string()
        print("\nlower method: ",str.lower(),"\n")
    
    elif(ch == 3):
        str=is_string()
        print("\nsplit method",str.split(),"\n")
    
    elif(ch == 4):
        str=is_string()
        print("\nstrip method: ",str.strip(),"\n")

    elif(ch == 5):
        break

    else:
        print("Invalid choice.. please try again.")
        
# good bye message
print()
print("-"*90)
print("\t\t\tThanks for visiting my Function CODE.")
print("-"*90,"\n")

