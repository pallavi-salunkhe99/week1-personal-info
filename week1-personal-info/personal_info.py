# Pallavi Salunkhe
#Project: Personal Information Manager
# My First Python Project

# here name is string data type used to store name value in name varibale 
# age is integer data type used to store age value in age varibale 
# city is string data type used to store city value in city varibale 
# hobby is string data type used to store hobby value in hobby varibale 

# Store static information
name="Pallavi Salunkhe"  
age=21
city="Pune"
hobby="Coding"

# Welcome message
print()
print("*"*40)
print("     Personal Information Manager     ")
print("*"*40)

# Get user input
print()
print("         Tell Me yourself ")
print()
print("-"*40)
food=input("What is Your Favorite Food: ")
color=input("What is Your Favorite Color: ")
print("-"*40)

# Calculate age in months
age_in_months = age * 12

# Display all information
print()
print("*"*40)
print("      Your Personal Information        ")
print("*"*40)
print(f"NAME: {name}")
print(f"AGE: {age} years ({age_in_months} months old)")
print(f"CITY: {city}")
print(f"HOBBY: {hobby}")
print()

# basic validation (check if input is empty)
if not food or not color:
    print("Error: Please enter both food and color.")
else:
 print(f"My Favorite Food is : {food}")
 print(f"My Favorite Color is : {color}")

# Goodbye message
print()
print("*"*40)
print("      Thanks for Looking My Program     ")
print("*"*40)

