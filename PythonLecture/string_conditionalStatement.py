# In python we can write string  using three different ways 
# it help to use multiple type quests 
# str1="This is string."
# str2='This is string'
# str3="""This is srting """

# escape sequence character.
# for next line we use \n
# for tab space we use \t
# str4="This is string.\nWe are creating it in Python."
# str5="This is string.\tWe are creating it in Python."
# print(str4)
# print(str5)

# basic operations
# 1. concatenation to use + 
# str1="Pallavi"
# str2="Salunkhe"
# Final_str=str1+str2
# print(Final_str)
# print(str1+str2)

# 2. length of str
# str1="Pallavi Salunkhe"
# print(len(str1))

# 3. indexing
# str="Pallavi"
# ch=str[6]
# print(ch)


# 4. slicing
# str="Pallavi"
# print(str[0:8])
# print(str[0:]) #[0:last index]
# print(str[:8]) # [zero index:to 8]
# print(str[1:len(str)])

# 4. slicing negating index 
# str="Apple"
# print(str[-3:-1])
# print(str[-5:-2])

# str="i am from studying python from ApnaCollege"
# print(str.endswith("app"))
# print(str.capitalize())
# print(str)
# print(str.replace("o","a"))
# print(str.find("o"))
# print(str.count("from"))

# Pratice question
# 1. WAP to input user's first name and print its length.
# print(" ="*40)
# print("\t\t\tWelcome To My First Program\t\t\t\t")
# print(" ="*40)
# First_name=input("\nEnter Your First Name: ")
# print("First Name: ", First_name)
# print("Its Length: ", len(First_name))

# 2. WAP to find the occurrence of '$' in a string 
# str="Hii i am the $ symbol $199.99"
# print(str.count("$"))


# Conditional Statements
# if-elif-else
# if
# age=21
# if(age>=18):
#     print("You can vote.")

# if-elif
# print("="*50)
# print("\t\tTraffi Signal System")
# print("="*50)
# light="Green"
# if(light == "Red"):
#     print("\nStop")
# elif(light == "Green"):
#     print("\nGo")
# elif(light == "Yellow"):
#     print("\nLook")

# print()
# print("-"*50)
# print("\t\tThank You for visiting..!")
# print("-"*50)

# if-elif-else
# print("="*50)
# print("\t\tTraffi Signal System")
# print("="*50)
# light="Red"
# if(light == "Red"):
#     print("\nStop")
# elif(light == "Green"):
#     print("\nGo")
# elif(light == "Yellow"):
#     print("\nLook")
# else:
#     print("Light color Broken")

# print()
# print("-"*50)
# print("\t\tThank You for visiting..!")
# print("-"*50)

# if-else
# age=10
# if(age>=18):
#     print("You can vote")
# else:
#     print("cannot vote.")

# print("="*50)
# print("\n\t\tStudent Grade System\n")
# print("="*50)
# mark=int(input("\nEnter Your Marks: "))
# if(mark >= 90):
#     print("Grade A")
# elif(mark>=80 and mark < 90):
#     print("Grade B")
# elif(mark >=70 and mark < 80):
#     print("Grade C")
# elif(mark <70 and mark>28):
#     print("Grade D")
# else:
#     print("Fail..")

# print()
# print("-"*50)
# print("\t\tThank You for visiting..!")
# print("-"*50)

# nesting
# age=90
# if(age >= 18):
#     if(age>= 80):
#         print("cannot drive")
#     else:
#          print("Can drive")
# else:
#     print("Cannot drive...")


# Practice Question
#1. WAP to check if a number entered by the user is odd or even.
# print()
# print("="*50)
# print("\t\tTo Check Number is ODD or Even")
# print("="*50)
# number=int(input("\nEnter a number: "))
# if(number%2==0):
#     print("Number is EVEN.")
# else:
#     print("Number is ODD.\n")
# print("-"*50)
# print("\t\tThank for using our code..!")
# print("-"*50)

# # 2. WAP to find the greatest of 3 numbers entered by user.
# print()
# print("="*70)
# print("\t\tTo Find the Greatest of 3 numbers entered by user")
# print("="*70)
# num1=int(input("\nEnter First Number: "))
# num2=int(input("Enter Second Number: "))
# num3=int(input("Enter Thired Number: "))
# if(num1 > num2 and num1 > num3):
#     print("\nNum1 is greater number.\n")
# elif(num2 > num1 and num2 > num3):
#     print("\nNum2 is grater number.\n")
# else:
#     print("\nNum3 is grater number.\n")
# print("-"*50)
# print("\t\tThank for using our code..!")
# print("-"*50)

# 3. WAP to check if a number is a multiple of 7 or not 
print()
print("="*70)
print("\tTo Check whether the number is multiple of 7 or not")
print("="*70)
num=int(input("\nEnter a number: "))
if(num%7==0):
    print("Number is multiple of 7.")
else:
    print("Number is not multiple of 7.")
print("-"*50)
print("\t\tThank for using our code..!")
print("-"*50)



