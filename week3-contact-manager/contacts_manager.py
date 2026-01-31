# Pallavi Salunkhe
# Project: Contact Management System
# Project Description: Build a comprehensive contact management system that stores names and phone numbers using dictionaries. 
#                     Implement functions to add, search, update, delete, and display contacts with proper validation and error handling.

print("\n","*"*90)
print("\n\t\t\t\tContact Management System\n")
print("*"*90,"\n")
contacts = {}
print("\n\t\t\t===== Welcome to Contact Management System =====\n\n")
while True:
    print("********** Menu **********\n")
    print("1. Add New Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. View All Contacts")
    print("6. Export to CSV")
    print("7. View Statistics")
    print("8. Exit\n")

    def validate_phonenumber(pho_number):
            if(pho_number.isdigit() and len(pho_number)==10 and pho_number[0] in "6789"):
                return True
            else:
                return False
            
    def validate_email(email_id):
        if( "@" in email_id and "." in email_id and email_id.index("@") < email_id.index(".")):
            return True
        else:
            return False
    
    ch=int(input("Enter your choice: \n"))
    print()
    # add contact
    if(ch == 1):
        name=input("Enter Name: ")
        
        # Phone validation
        while True:
            pho_number=input("Enter Phone Number: ")
            if validate_phonenumber(pho_number):
                break
            else:
                print("Invalid phone number! Enter 10-digit number.")

    
        # Email validation
        while True:
            email_id=input("Enter Email ID: ")
            if(validate_email(email_id)):
                break
            else:
                print("Invalid email! Try again.")

        address=input("Enter Address: ")
        company=input("Enter Company Name: ")

        contacts[name]={
            "pho_number": pho_number,
            "email_id": email_id,
            "address" :address,
            "company" :company
        }
        print("\n New Contact added succsufully. \n")

    # search contact
    elif(ch == 2):
        name=input("Enter name to search contact: ")
        print()
        if(name in contacts):
            info =contacts[name]
            print("-"*50)
            print("\nPhone Number: ",info["pho_number"])
            print("Email ID: ",info["email_id"])
            print("Address:",info["address"])
            print("Company Name:",info["company"],"\n")
            print("-"*50)
            print()
        else:
            print("contact not found.")


    # update contact
    elif(ch == 3):
        name=input("Enter name to update Phone Number: ")
        if(name in contacts):
            contacts[name]["pho_number"] = input("Enter New Phone Number: ")
            print("\n phone number updated succsufully. \n")
        else:
            print("contact not found.")
    
    # delete ontact
    elif(ch == 4):
        name=input("Enter name to delete contact Data: ")
        if(name in contacts):
            del contacts[name]
            print("\n contact Data deleted succsufully. \n")
        else:
            print("contact not found.")
    
    # view contacts
    elif(ch == 5):
        print("="*50)
        print("\t\tView Contact Data")
        print("="*50)
        for name, info in contacts.items():
            print("\nName: ",name)
            print("Phone Number: ",info["pho_number"])
            print("Email ID: ",info["email_id"])
            print("Address:",info["address"])
            print("Company Name:",info["company"])
            print("-"*50)
        print() 
        print("="*50)
        print("\t\txxxxxxxxxxxxxxxxxxxxx")
        print("="*50)    
        print("\n\n")


    # Export to CSV
    elif(ch == 6):
        import csv
        with open("contacts.csv", "w", newline="") as file:
            writer = csv.writer(file)
            
            # write header
            writer.writerow(["Name", "Phone Number", "Email ID", "Address", "Company Name"])

            # write contact data
            for name, info in contacts.items():
                writer.writerow([
                name,
                info["pho_number"],
                info["email_id"],
                info["address"],
                info["company"]
            ])

        print("\nContacts exported to contacts.csv successfully!\n")

    
    # View Statistics
    elif(ch == 7):
        print("="*50)
        print("\t\tView Statistics")
        print("="*50)
        total =len(contacts)
        
        for info in contacts.values():
            total=total
            
        print("\n\t****** Contact Statistics ******\n")
        print("Total contacts:", total)
        print() 
        print("="*50)
        print("\t\txxxxxxxxxxxxxxxxxxxxx")
        print("="*50)    
        print("\n\n")

     # Exit menu
    elif(ch == 8):
        break

    else:
        print("\n Invalid choice.. please try again. \n")

print()
print("-"*90)
print("\t\t\tThanks for visiting my Contact Management System.")
print("-"*90,"\n")