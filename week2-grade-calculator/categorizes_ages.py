# Q. 2 Build a program that categorizes ages into groups.
# here i use if/elif/else condition statements.

print()
print("*"*90)
print("\t\t\tCategorizes Ages Into Groups System")
print("*"*90)
print()
age=int(input("Enter age:"))
print()
print(" ***** \tAge-wise Population Groups  *****\n")
if(age >=0 and age<=14):
    print("You are in Child age group.")
elif(age >= 15 and age <= 24):
    print("You are in Youth age group.")
elif(age >= 25 and age <= 64):
    print("You are in Adult age group.")
elif(age >=65):
    print("You are in Senior age group.")
else:
    print("Wrong enter age value..! please try again.")
print()
print("-"*90)
print("\t\t\tThanks for visiting me My Python Program..!")
print("-"*90)


