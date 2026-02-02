# 1. Create a program that saves user data to a text file.

print()
print("*"*90)
print("\t\t\t Saves user data into Text File")
print("*"*90,"\n")

print("\t","="*70)
print("\t\t\t\tEnter User Data")
print("\t","="*70)

print()
id = input("\t Enter User ID: ")
name = input("\t Enter User Name: ")
phone_number = input("\t Enter Phone Number: ")
address = input("\t Enter Address: ")

print("\n\t user data saved in text file succsfully.")

# to cerate file and save data in text file.
f=open("userdata.txt","a")
f.write(id + "\t" + name + "\t" + phone_number + "\t" + address + "\n")
f.close()

print("-"*90)
print("\t\t\tThanks for looking my python code.")
print("-"*90,"\n")