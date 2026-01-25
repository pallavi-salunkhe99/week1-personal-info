# Q 7.Implement error handling for user inputs
# to handle errors in when user only enter number ont any other character for calculating addtions of two numbers.
print("\n")
print("*"*70)
print("\t\tUser Input Error Handling Program")
print("*"*70)
print("\n")

try:
    number1=int(input("Enter First Number: "))
    number2=int(input("Enter Second Number: "))
    add=number1+number2
    print("Addition: ",add ,"\n")
except ValueError:
    print("Please enter numbers only.\n")

print()
print("-"*70)
print("\t\tThanks for visiting me My Python Program..!")
print("-"*70)
print()