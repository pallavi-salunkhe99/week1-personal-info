# Q.4 Create a multiplication table generator
# here i use for loop to print n number multiplication table. 
# and also use range function which represent start value from 1 to print 10. 

print()
print("*"*90)
print("\t\tMultiplication Table Generator System")
print("*"*90)
number=int(input("Enter a Number: "))
for i in range(1,11):
    print(number, " * ",i, " = ",number*i)

print()
print("-"*90)
print("\t\tThanks for visiting me My Python Program..!")
print("-"*90)
