# 3.Create a student database using dictionaries.

# welcome message
print()
print("*" *90)
print("\t\t\t\tStudent Database Dictionaries")
print("*" *90,"\n")

students ={}
while True:
    print("********** Menu **********\n")
    print("1. Add student")
    print("2. Delete Student Data")
    print("3. View Students Data")
    print("4. Update student Data")
    print("5. Exit\n")

    ch = int(input("Enter Your choice: "))

    # add students
    if(ch == 1):
        rollno = int(input("Enter Roll NO (should be start from 1): "))
        name = input("Enter Student Name: ")
        year = input("Enter Your Year(FE,SE,TE,BE): ")
        branch = input("Enter Branch Name: ")
        cgp = float(input("Enter Your CGPA: "))

        students [rollno]={

        "name" : name,
        "year":year,
        "branch":branch,
        "cgp": cgp}
        print("\nStudent addeded succufully.\n")
    
    # delete students 
    elif(ch == 2):
        rollno=int(input("Enter Roll No to delete: "))
        print("\ndelete\n")
        if(rollno in students):
            del students[rollno]
            print("\nstudent data deleted succufully.\n")
        else:
            print("\nstudent not found.\n")


    # view students
    elif(ch == 3):
        print("\nview\n")
        if(not students):
            print("\n No students in database.\n")
        else:
            print("-"*60)
            print("\n********** Display Student Data **********\n")
            print("-"*60)
            print()
            print("RollNo\t | Name\t | Year\t | Branch | CGP ")
            for rollno, info in students.items():
                print(rollno,"\t | ",info["name"],"\t | ",info["year"],"   | ",info["branch"],"    | ",info["cgp"])
            print("\n")


    # update students 
    elif(ch == 4):
        rollno=int(input("Enter Roll No to update: "))
        if(rollno in students):
            students[rollno]["cgp"]= float(input("Enter new CGP: "))
            print("\nstudent data updated succufully.\n")
        else:
            print("student not found.")


    elif(ch == 5):
        break
    else:
        print("Invalid choice please try again..!")

        
# good bye message
print()
print("-"*90)
print("\t\t\tThanks for visiting my Function CODE.")
print("-"*90,"\n")

