# Pallavi Salunkhe
# Project: Student Grade Calculator
# Project Description: Build a comprehensive grade calculator that takes multiple student marks, calculates grades with comments, 
#                      stores results in a list, and provides statistics. 

# welcome message
print()
print("*" *90)
print("\t\t\t\tStudent Grade Calculator System")
print("*" *90)
print()


# Define Grading System

# grade based on marks function
def grade_calcu(grade):
    if(grade > 90 and grade <= 100):
        return("A")
    elif(grade > 80 and grade <= 90):
        return("B")
    elif(grade > 70 and grade <=80):
        return("C")
    elif(grade >=28 and grade <=70):
        return("D")
    elif(grade < 28):
        return("Fail")

# grade comments sunction 
def grade_comments(grade):
    if(grade > 90 and grade <= 100):
        return("Excellent! Keep up the great work!")
    elif(grade > 80 and grade <= 90):
        return("Very Good! You\'re doing well.")
    elif(grade > 70 and grade <=80):
        return("Good. Room for improvement.")
    elif(grade <=70):
        return("Needs Improvement. Please study more.")
    elif(grade < 28):
        return("Failed. Please seek help from teacher.")

#  Get Student Information
print("")
while True:
    print("\n----------- Operation Menu -----------\n")
    print("1. Input Student Number")
    print("2. RESULTS SUMMARY")
    print("3. CLASS STATISTICS")
    print("4. Search Student")
    print("5. Exit")
    print()

    ch=int(input("Enter Your Choice: "))
    print()
    

    if(ch == 1):
        student=int(input("\nEnter number of students: "))
        print()

        # Collect Data
        allStudents = [] #main student info list

        for i in range(1,student+1):
            print("*********** Student",i, "***********\n")
            student_name=input("Student Name: ")
            print("Enter Marks (0-100): ")
            math=int(input("Math: "))
            science=int(input("Science: "))
            english=int(input("English: "))
            # list of one student 
            studentInfoList=[]
            studentInfoList.append(student_name)
            studentInfoList.append(math)
            studentInfoList.append(science)
            studentInfoList.append(english)
            allStudents.append(studentInfoList)
            print()


    elif(ch == 2):
        # RESULTS SUMMARY
        print("="*90)
        print("\t\t\t\tRESULTS SUMMARY")
        print("="*90)
        print("Name\t\t\t| Avg\t\t| Grade\t\t| Comment\n")
        print("-"*90)
        result_list=[]

        for i in allStudents:
            total=i[1]+i[2]+i[3]
            grade=total/3
            print(i[0],"\t\t\t|",round(grade,1),"\t\t|",grade_calcu(grade),"\t\t|",grade_comments(grade),"\n")
            result_list.append(grade)

    elif(ch == 3):
        # CLASS STATISTICS
        print("="*90)
        print("\t\t\t\tCLASS STATISTICS")
        print("="*90)
        print("Total Students:", student)

        class_avg=sum(result_list)/len(result_list)
        print("Class Average:",round(class_avg,1))

        highest=max(result_list)
        print("Highest Average:",highest)

        lowest=min(result_list)
        print("Lowest Average: ",lowest)
    
    elif(ch == 4):
        name = input("Enter student name to search: ")
        print(allStudents)
    
    elif(ch == 5):
        print()
        print("-"*90)
        print("\t\t\tThanks for visiting me My Python Program..!")
        print("-"*90)
        print()
        break
    else:
        print("Wrong choice please try again..!")


    # good bye message
    print()
    print("-"*90)
    print("\t\t\tThanks for visiting me My Python Program..!")
    print("-"*90)
    print()
